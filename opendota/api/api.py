import requests
import json


def get_query(end_point, **kwargs):
    url = 'https://api.opendota.com/api/' + end_point
    response = requests.get(url, params=kwargs)
    if response.status_code != requests.codes.ok:
        print('Received HTTP Error: %d' % response.status_code)
        print('Response: ' + response.text)
        print(url)
        print(kwargs)
        return ''
    else:
        try:
            return response.json()
        except ValueError:
            return response.text


def sql_query(query_string):
    results = get_query('explorer', sql=query_string)
    return results['rows']
