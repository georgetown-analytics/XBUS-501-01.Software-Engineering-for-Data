# nba
# Analyzes the NBA Salary to PER data set
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sat Sep 20 09:35:11 2014 -0400
#
# Copyright (C) 2014 Bengfort.com
# For license information, see LICENSE.txt
#
# ID: nba.py [] benjamin@bengfort.com $

"""
Analyzes the NBA Salary to PER data set with a visualization
"""

##########################################################################
## Imports
##########################################################################

import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

PATH = os.path.abspath('fixtures/nba_players.csv')

def read_data(path=PATH):
    return pd.DataFrame(pd.read_csv(PATH))

def graph_data(path=PATH, xkey='PER', ykey='SALARY'):
    data = read_data(path)
    xval = data['PER']
    yval = data['SALARY']

    fig,axe = plt.subplots()
    plt.scatter(xval, yval, alpha=0.7)
    plt.ylim([-10000, data['SALARY'].max()+500000])

    plt.ylabel('salary')
    plt.xlabel('player efficiency rating')
    plt.title('NBA 2013 Player Efficieny Rating and Salary Correlation')

    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    graph_data()
