import requests
from requests import RequestException

#Make the REST request GET request
resp = requests.get('https://opendata.vancouver.ca/api/records/1.0/search/?dataset=schools', {'refine.geo_local_area': 'Kitsilano'})
if resp.status_code != 200:
    # This means something went wrong.
    raise RequestException('GET /tasks/ {}'.format(resp.status_code))

records = resp.json()['records']

print("There are", len(records), "records")

for k in records:
    print(k)