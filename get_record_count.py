import requests
from requests import RequestException


def get_data(dataset_name: str, area: str) -> int:
    '''
    Get a record count of data from the Vancouver OpenData.... repository.

    @param dataset_name:
    @param area: the 'geo_local_area'. In Vancouver this maps to the neighbourhood (eg. Kitsilano, Hastings-Sunrise)
    @precondition: the number of records is returned
    @return: int
    '''

    params = {'refine.get_local_area': area}
    resp = requests.get('https://opendata.vancouver.ca/api/records/1.0/search/dataset=' + dataset_name, data=params)
    if resp.status_code != 200:
        # This means something went wrong.
        raise RequestException('GET /tasks/ {}'.format(resp.status_code))

    return resp.json()['nhits']