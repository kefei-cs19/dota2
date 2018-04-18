from api_key import API_KEY
from opendota.api import api as openapi

import dota2api
import json

if __name__ == '__main__':
    # steam official api
    api = dota2api.Initialise(API_KEY)
    result = api.get_match_details(3816957355)
    print(json.dumps(json.loads(result.json), indent=2))

    #open dota api
    result = openapi.get_query('matches/3816957355')
    print(json.dumps(result, indent=2))
