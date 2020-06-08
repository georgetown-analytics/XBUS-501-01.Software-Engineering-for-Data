# tests.test_buildings
# test module to evaluate the classes in the buildings module
#
# to execute tests, run the following command from project root:
#   pytest tests
#
# for a list of available asserts:
# https://docs.pytest.org/en/latest/assert.html
#
# Author:     Allen Leis <allen.leis@georgetown.edu>
# Created:    Fri Sep 11 23:22:32 2015 -0400
# Adapted by: Rebecca Bilbro <rsb89@georgetown.edu>
# Updated on: Thu Mar 5 14:20:08 EST 2020
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_buildings.py [] allen.leis@georgetown.edu $

"""
Test cases for buildings module
"""

##########################################################################
## Imports
##########################################################################

import pytest

from motorsports.buildings import Car
from motorsports.buildings import Garage

##########################################################################
## Tests
##########################################################################


class TestGarage():

    def test_has_name(self):
        """
        Ensure the garage returns the name provided at creation
        """
        name = "Bob's Garage"
        garage = Garage(name)
        assert name == garage.name

    def test_allows_cars_to_enter(self):
        """
        Ensure vehicle is in garage after it enters (eg: vehicle in garage == True)
        """
        garage = Garage("Bob's Garage")
        car = Car("Blue", "Toyota", "Camry")
        garage.enter(car)

        assert garage._vehicles[0] == car
        assert len(garage._vehicles) == 1

    def test_only_allows_cars_to_enter(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to enter

        see https://docs.pytest.org/en/stable/reference.html#pytest-raises
        """
        garage = Garage("Bob's Garage")
        with pytest.raises(TypeError):
            garage.enter(42)

    def test_only_allows_cars_to_exit(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to exit

        see https://docs.pytest.org/en/stable/reference.html#pytest-raises
        """
        garage = Garage("Bob's Garage")
        with pytest.raises(TypeError):
            garage.exit(42)

    def test_allows_cars_to_exit(self):
        """
        Ensure vehicles leave the garage
        """
        garage = Garage("Bob's Garage")
        car = Car("Blue", "Toyota", "Camry")
        garage.enter(car)
        garage.exit(car)

        assert len(garage._vehicles) == 0

    def test_raise_lookup_error_on_exit(self):
        """
        Ensure that garage raises LookupError if vehicle attempts
        to exit but was never in garage.
        """
        garage = Garage("Bob's Garage")
        car = Car("Blue", "Toyota", "Camry")
        with pytest.raises(LookupError):
            garage.exit(car)

    def test_iter_builtin(self):
        """
        Ensure we can iterate over garage vehicles by trying to
        iterate over the garage itself
        """
        name = "Bob's Garage"
        garage = Garage(name)
        car1 = Car("white", "Toyota", "Camry")
        car2 = Car("black", "Toyota", "Camry")
        garage.enter(car1)
        garage.enter(car2)
        for car in garage:
            assert car in garage

    def test_len_builtin(self):
        """
        Ensure that the length of the garage matches the number
        of vehicles parked in it
        """
        name = "Bob's Garage"
        garage = Garage(name)
        car1 = Car("white", "Toyota", "Camry")
        car2 = Car("black", "Toyota", "Camry")
        garage.enter(car1)
        garage.enter(car2)
        assert len(garage) == 2
