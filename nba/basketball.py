# basketball.py

# NBA Player Statistics Workshop for the
# Georgetown University Data Science Certificate Program
# 09/19/2015
# by Ben Benfort and Rebecca Bilbro



"""
Welcome!

The NBA Player Statistics Workshop:

Given a dataset of NBA players performance and salary in 2014, use Python to
load the dataset and compute the summary statistics for the SALARY field:
- mean
- median
- mode
- minimum
- maximum

You will need to make use of the csv module to load the data and interact with
it. Computations should require only simple arithmetic. (For the purposes of
this exercise, attempt to use pure Python and no third party dependencies like
Pandas - you can then compare and contrast the use of Pandas for this task
later).

Bonus:
Determine the relationship of PER (Player Efficiency Rating) to Salary via a
visualization of the data.


URL for NBA 2014 Players Dataset => http://bit.ly/gtnbads
"""

#####################################################
# Imports
#####################################################
"""
You'll need some of these later, but it's traditional to put them
all at the beginning.
"""
import os
import csv
import json

from collections import Counter
from operator import itemgetter
from urllib.request import urlopen

#####################################################
# Fetching the Data
#####################################################
"""
You have a couple of options of fetching the data set to begin your analysis:
Cut and past the link above and download the file.
Write a Python function that automatically downloads the data as a
comma-separated value file (CSV) and writes it to disk.

In either case, you'll have to be cognizant of where the CSV file lands.
Here is a quick implementation of a function to download a URL at a file and
write it to disk.

Note the many approaches to do this as outlined here: How do I download a file
over HTTP using Python?:
http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
"""


def download(url, path):
    """
    Downloads a URL and writes it to the specified path. The "path"
    is like the mailing address for the file - it tells the function
    where on your computer to send it!

    Also note the use of "with" to automatically close files - this
    is a good standard practice to follow.
    """
    response = urlopen(url)
    with open(path, 'wb') as f:
        f.write(response.read())

    response.close()

"""
Your turn: use the above function to download the data!
"""
## Write the Python to execute the function and download the file here:







#####################################################
# Loading the Data
#####################################################
"""
Now that we have the CSV file that we're looking for, we need to be able to
open the file and read it into memory. The trick is that we want to read only a
single line at a time - consider really large CSV files. Python provides memory
efficient iteration in the form of generators and the csv.reader module exposes
one such generator, that reads the data from the CSV one row at a time. Moreover,
we also want to parse our data so that we have specific access to the fields
we're looking for. The csv.DictReader class will give you each row as a
dictionary, where the keys are derived from the first, header line of the file.
Here is a function that reads data from disk one line at a time and yields it to
the user.
"""
def read_csv(path):
    # First open the file
    with open(path, 'rt') as f:
        # Create a DictReader to parse the CSV
        reader = csv.DictReader(f)
        for row in reader:
            # HINT: Convert SALARY column values into integers & PER column into
            # floats. Otherwise CSVs can turn ints into strs!
            # You'll thank me later :D
            row['SALARY'] = int(row['SALARY'])
            row['PER'] = float(row['PER'])
            # Now yield each row one at a time.
            yield row
"""
Your turn: use the above function to open the file and print out the first row
of the CSV! To do this, you'll need to do three things:

First, remember where you told the download function to store your file?
Pass that same path into read_csv:
"""
## Write the Python to execute our read_csv function.




"""
Next step: The read_csv function "returns" a generator. How can we access just
the first row? Remember how to access the next row of a generator?
HINT: http://stackoverflow.com/questions/4741243/how-to-pick-just-one-item-from-a-generator-in-python
"""
## Now write the Python to print the first row of the CSV here.




"""
Are there different ways to print the first n rows of something? Sure! Try using break, which will stop a for loop from running. E.g. the code:
for idx in xrange(100):
    if idx > 10:
        break
...will stop the for loop after 10 iterations.
Next, write a for loop that can access and print every row.
"""
## Write the Python to print *every* row of the CSV here.




#####################################################
# Summary Statistics
#####################################################
"""
In this section, you'll use the CSV data to write computations for mean, median,
mode, minimum, and maximum. Use Python to access the values in the SALARY column.
"""
data = list(read_csv('fixtures/nba_players.csv')) #Put in your own path here.
data  = sorted(data, key=itemgetter('SALARY'))

total = 0
count = 0

for row in data:
        count += 1
        total += row['SALARY']


# Total Count
print("There are {0:d} total players.".format(count))


# Write the Python to get the median
median =
print("The median salary is {0:d}.".format(median))


# Write the Python to get the minimum
minimum =
print("The minimum salary is {0:d}.".format(minimum))


# Write the Python to get the maximum
maximum =
print("The maximum salary is {0:d}.".format(maximum))


# Write the Python to get the mean
mean =
print("The mean salary is {0:d}.".format(mean))



"""
Nice work! Now... calculating the mode is a bit different. Remember about the
Decorate-Sort-Undecorate pattern that we learned about in ThinkPython? That
will work here!

Reminder: http://www.greenteapress.com/thinkpython/html/thinkpython013.html
"""
## Write the Python to get the mode of the salaries.




"""
The "DSU" approach is a little inefficient. Instead of using a dictionary as
our data type to solve the mode problem, we could use counter() from the
Collections module. Read more about counter() and try it out here:
https://pymotw.com/2/collections/counter.html
"""
## Experiment with using counter() here.






#####################################################
# Putting the pieces together
#####################################################
"""
The above summary statistics can actually be computed inside of a single
(and elegant!) function. Give it a try!
"""

def statistics(path):
    """
    Takes as input a path to `read_csv` and the field to
    compute the summary statistics upon.
    """

    # Uncomment below to load the CSV into a list
    # data = list(read_csv(path))

    # Fill in the function here




    stats = {
        'maximum': data[-1]['SALARY'],
        'minimum': data[0]['SALARY'],
        'median': data[count // 2]['SALARY'], # Any potential problems here?
        'mode': freqs.most_common(2),
        'mean': total // count,
    }

    return stats
{
    "minimum": null,
    "median": null,
    "mode": null,
    "maximum": null,
    "mean": null
}


"""
Keep playing with the above function to get it to work more efficiently or to
reduce bad data in the computation - e.g. what are all those zero salaries?
"""




#####################################################
# Visualization
#####################################################
"""Congratulations if you've made it this far! It's time for the bonus round!
You've now had some summary statistics about the salaries of NBA players,
but what we're really interested in is the relationship between SALARY and
the rest of the fields in the data set. The PER - Player Efficiency Rating,
is an aggregate score of all performance statistics; therefore if we determine
the relationship of PER to SALARY, we might learn a lot about how to model NBA
salaries.

In order to explore this, let's create a scatter plot of SALARY to PER, where
each point is an NBA player. Visualization is going to require a third party
library. You probably already have matplotlib, so that might be the simplest
if you're having trouble with installation. If you don't, pip install it now!
Follow the documentation to create the scatter plot inline in the notebook in
the following cells.
"""
# Fill in the blanks below to create the visualization here
import os
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def read_data(path):
    # Pandas is an efficient way to wrangle the data quickly
    return pd.DataFrame(pd.read_csv(path))

def graph_data(path, xkey='PER', ykey='SALARY'):
    data = read_data(path)
    ## Fill this in yourself!
    plt.show()

graph_data('fixtures/nba_players.csv') # Or whatever your path is






"""
Nice work!! Matplotlib is pretty useful, but also kind of bare bones. Once you're ready to experiment with other libraries and take your visualizations to the next level, check out the following:
-Seaborn
-Bokeh
-Pandas

Our favorite is Bokeh - it's interactive!
"""
