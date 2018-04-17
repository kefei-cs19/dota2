from api_key import API_KEY

import dota2api
import json

if __name__ == '__main__':
    api = dota2api.Initialise(API_KEY)
    result = api.get_match_details(3816957355)
    print(json.dumps(json.loads(result.json), indent=2))
