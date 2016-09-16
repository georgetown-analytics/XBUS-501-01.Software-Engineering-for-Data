# per
# Analyzes the NBA Salary to PER data set
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 20 09:35:11 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: per.py [] benjamin@bengfort.com $

"""
Computes summary statistics for the nba_players.csv file
"""

##########################################################################
## Imports
##########################################################################

import csv

from collections import Counter
from operator import itemgetter

##########################################################################
## Analysis functions
##########################################################################

def load_data(path):
    """
    Loads the data from a file into a list.
    """
    with open(path, 'r') as data:
        reader = csv.DictReader(data)
        for row in reader:
            row['SALARY'] = int(row['SALARY'])
            row['PER'] = float(row['PER'])
            yield row

def statistics(path):
    data  = list(load_data(path))
    data  = sorted(data, key=itemgetter('SALARY'))

    count = 0
    total = 0.0
    freqs = Counter()

    for row in data:
        count += 1
        total += row['SALARY']
        freqs[row['SALARY']] += 1

    stats = {
        'maximum': data[-1]['SALARY'],
        'minimum': data[0]['SALARY'],
        'median': data[count // 2]['SALARY'],
        'mode': freqs.most_common(2),
        'mean': total // count,
    }

    return stats

if __name__ == '__main__':
    import json
    print(json.dumps(statistics('fixtures/nba_players.csv'), indent=4))
