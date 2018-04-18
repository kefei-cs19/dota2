import requests


def get_query(end_point, **kwargs):
    url = 'https://api.opendota.com/api/' + end_point
    response = requests.get(url, params=kwargs)
    if response.status_code != requests.codes.ok:
        return ''
    else:
        try:
            return response.json()
        except ValueError:
            return response.text


def sql_query(query_string):
    results = get('explorer', sql=query_string)
    return results.rows
