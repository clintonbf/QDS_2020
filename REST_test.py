import requests
from requests import RequestException

#Make the REST request GET request
#Here we're asking for rental properties with outstanding (ie. unresolved) issues
resp = requests.get('https://opendata.vancouver.ca/api/records/1.0/search/?dataset=rental-standards-current-issues')
if resp.status_code != 200:
    # This means something went wrong.
    raise RequestException('GET /tasks/ {}'.format(resp.status_code))

records = resp.json()['records']

print("There are", len(records), "records")

for k in records:
    print(k)