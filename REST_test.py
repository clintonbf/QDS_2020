import requests
from requests import RequestException

dataset = input("Which dataset do you want (type it exactly)")
region = input("Specify your neighbourhood (press enter for none)")

# Make the REST request GET request
# Here we're asking for rental properties with outstanding (ie. unresolved) issues
if region:
    resp = requests.get('https://opendata.vancouver.ca/api/records/1.0/search/?dataset=' + dataset,
                        params={'refine.geo_local_area': region})
else:
    resp = requests.get('https://opendata.vancouver.ca/api/records/1.0/search/?dataset=' + dataset)

if resp.status_code != 200:
    # This means something went wrong.
    raise RequestException('GET /tasks/ {}'.format(resp.status_code))

print("You searched for '{}'".format(resp.url))
print("There are {} records".format(resp.json()['nhits']))

# Grab the data records
records = resp.json()['records']

for k in records:
    print(k)