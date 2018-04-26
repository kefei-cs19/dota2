from opendota.api import api as openapi

import argparse
import json
import time

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-n',
        '--numMatches',
        type=int,
        dest='num_matches',
        default=1000,
        help='Number of most recent pro matches to scrape',
    )
    parser.add_argument(
        '-o',
        '--output',
        dest='filename',
        default='match_log.txt',
        help='File path to the output file; will overwrite if file already exists',
    )
    return parser.parse_args()


def download_matches(numMatches, filename):
    query_string = """
        SELECT
            matches.match_id,
            matches.start_time
        FROM matches
        WHERE TRUE
        ORDER BY start_time DESC NULLS LAST
        LIMIT %d
    """ % numMatches

    match_list = openapi.sql_query(query_string)

    with open(filename, 'w') as f:
        count = 0
        for match in match_list:
            match_detail = openapi.get_query('matches/%d' % match['match_id'])
            f.write(json.dumps(match_detail))
            f.write('\n\n')
            count += 1
            print('%d matches downloaded.' % count)
            time.sleep(1) # access to this api is severely rate limited


if __name__ == '__main__':
    args = parse_args()
    download_matches(args.num_matches, args.filename)