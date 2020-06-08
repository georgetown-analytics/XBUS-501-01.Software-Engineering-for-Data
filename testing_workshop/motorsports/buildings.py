# motorsports.buildings
# description
#
# Sample Usage:
#    g = Garage("Al's Garage")
#    c = Car('silver', 'Porsche', 'Boxster')
#    g.enter(c)
#    g.exit(c)
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: buildings.py [] allen.leis@georgetown.edu $

"""
A module to supply building related classes
"""

##########################################################################
## Imports
##########################################################################

from motorsports.vehicles import BaseVehicle, Car

##########################################################################
## Classes
##########################################################################

class BaseBuilding(object):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class Garage(BaseBuilding):

    def __init__(self, *args, **kwargs):
        self._vehicles = []
        super(Garage, self).__init__(*args, **kwargs)

    def enter(self, vehicle):
        """
        Adds a new vehicle to the garage
        """
        if isinstance(vehicle, BaseVehicle):
            self._vehicles.append(vehicle)
            print('The {} has been parked in {}.'.format(vehicle.description, self.name))
        else:
            raise TypeError('Only vehicles are allowed in garages')

    def exit(self, vehicle):
        """
        Removes a vehicle from the garage
        """
        if isinstance(vehicle, BaseVehicle):
            if vehicle not in self:
                raise LookupError('That vehicle is not in {}.'.format(self.name))
            self._vehicles.remove(vehicle)
            print('The {} has left {}.'.format(vehicle.description, self.name))

        else:
            raise TypeError('Only vehicles are allowed in garages.')

    def __len__(self):
        """
        Python builtin to support len function
        """
        return len(self._vehicles)

    def __iter__(self):
        """
        Python builtin to support iteration
        """
        for v in self._vehicles:
            yield v
