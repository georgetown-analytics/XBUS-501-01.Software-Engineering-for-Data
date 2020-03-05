# motorsports.vehicles
# description
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: vehicles.py [] allen.leis@georgetown.edu $

"""
A module to supply building related classes
"""

##########################################################################
## Imports
##########################################################################


##########################################################################
## Classes
##########################################################################

class BaseVehicle(object):

    def __init__(self):
        self._state = None

    @property
    def state(self):
        """
        return a string describing the state of the vehicle
        """
        return self._state or 'stopped'

    @property
    def description(self):
        """
        return a string describing this object
        """
        return self.__class__.__name__

    def start(self):
        """
        Starts the vehicle
        """
        self._state = 'started'

    def shutdown(self):
        """
        Starts the vehicle
        """
        self._state = 'stopped'

    def __str__(self):
        return "I am a {}.".format(self.description)


class Car(BaseVehicle):

    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model
        super(Car, self).__init__()

    @property
    def description(self):
        """
        return a string describing this object
        """
        return '{} {} {}'.format(self.color, self.make, self.model)

    def start(self):
        """
        Starts the vehicle
        """
        super(Car, self).start()
        print('vroom')


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    c = Car('white', 'Ford', 'Bronco')
    print(c.state)
    c.start()
    print(c.state)
