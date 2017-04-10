
import sys
import grequests

fl = open('JA_ATL_ITEM_DIM_part1.json', encoding='latin-1')

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik16UTFNMEkwT1RrMk9URTFSRVJCUmprek5Ua3dNMFEwTXpoQlJrTXpSamRFTkRRMFJUUXhPQSJ9.eyJpc3MiOiJodHRwczovL2xveWFsdHlvbmUtc2FuZGJveC5hdXRoMC5jb20vIiwic3ViIjoicGluZ2ZlZGVyYXRlfExNYTJAbG95YWx0eS5jb20iLCJhdWQiOiJlSnZBcnptek82SzNzNU43QlVKdG5DQm9mRUdveWJuQiIsImV4cCI6MTQ5MTI3NzM0NywiaWF0IjoxNDkxMjQxMzQ3fQ.J7NKSNPElrPmSLcfim3DYiS3X2lJGFG4cgNeKK01bmAOvFwiBjEnQgfSYprg7dixxn5vJn-3QaTKSaSmKtgcZDprpoFvqVzZXMvjzQCWi4q9ODSgFDqvRMD8Wt-DKyTW3BbHzGdC_HEVmWRFC2C10p0_h9uy17PYCwE6qA0a9l61UrCmTj2j3QWF7eZRbqzlyeDfJfQQ4s9sfnYtJZD9rOGlm6iTCxAt2_f4VjMtrUShOPdq6Gatyv-pR-R2FxTcrYVvk7rkQ_o47-osJ8Fa3YFJJeQZZJXfl6i7YM3Iy3KmgaTnUhTOsX2rYr6OvolD9y5PEXCBa-UGmJC0kBQtgw"

request_header = {
    'content-type': 'application/json',
    'Authorization': 'Bearer %s' % token,
    'ptoken': "w2OhRjKdUTibzmINw33PAaCN"
}

stream_name = "catalyst_stream_api1"

api_url = "https://sandbox.api.loyalty.com/v2/dh-spine/streams/%s" % stream_name



requests_list = []
responses_500 = []
data = ''

counter = 0

from datetime import datetime

now = datetime.now()



for line in fl:

    data += line + '\n'

    if sys.getsizeof(data) >= 900000:
        requests_list.append(grequests.post(api_url, headers=request_header, data=data))
        data = ''

    if len(requests_list) == 5:
        responses = grequests.map(requests_list)
        requests_list = []

        for resp in responses:
            if resp.status_code != 200:
                responses_500.append(resp)
                print(resp.status_code)

    counter += 1

    if counter >= 10:
        break

    if counter % 1000 == 0:
        print('{} records processed'.format(counter))

fl.close()

print(datetime.now() - now)

print('{} Failed requests'.format(len(responses_500)))