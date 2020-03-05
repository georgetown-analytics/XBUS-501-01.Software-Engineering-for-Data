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
        name = 'Bob\'s Garage'
        g = Garage(name)
        assert name == g.name

    @pytest.mark.skip(reason="pending test code")
    def test_allows_cars_to_enter(self):
        """
        Ensure the garage allows Car object to enter
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_ensure_cars_enter_fully(self):
        """
        Ensure vehicle is in garage after it enters (eg: vehicle in garage == True)
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_only_allows_cars_to_enter(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to enter
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_only_allows_cars_to_exit(self):
        """
        Ensure the garage raises TypeError if non vehicle attempts to exit
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_allows_cars_to_exit(self):
        """
        Ensure vehicles can leave the garage
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_ensure_cars_exit_fully(self):
        """
        Ensure vehicle is not in garage after it exits
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_raise_lookup_error_on_exit(self):
        """
        Ensure that garage raises LookupError if vehicle attempts
        to exit but was never in garage.
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_iter_builtin(self):
        """
        Ensure we can iterate over garage vehicles by trying to
        iterate over the garage itself
        """
        pass

    @pytest.mark.skip(reason="pending test code")
    def test_len_builtin(self):
        """
        Ensure that the length of the garage matches the number
        of vehicles parked in it
        """
        pass
