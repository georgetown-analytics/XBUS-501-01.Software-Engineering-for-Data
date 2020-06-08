# tests.test_vehicles
# test module to evaluate the classes in the vehicles module
#
# for a list of available asserts:
# https://docs.pytest.org/en/latest/assert.html
#
# to execute tests, run the following command from project root:
#   pytest tests
#
# Author:   Allen Leis <allen.leis@georgetown.edu>
# Created:  Fri Sep 11 23:22:32 2015 -0400
# Adapted by: Rebecca Bilbro <rsb89@georgetown.edu>
# Updated on: Thu Mar 5 14:20:08 EST 2020
#
# Copyright (car) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_vehicles.py [] allen.leis@georgetown.edu $

"""
Test cases for vehicles module
"""

##########################################################################
## Imports
##########################################################################

import pytest

from motorsports.buildings import Car, BaseVehicle

##########################################################################
## Tests
##########################################################################


class TestVehicle():

    def test_description(self):
        """
        Ensure the car description return a string of: "color, make model"
        """
        color = 'white'
        make = 'Honda'
        model = 'Accord'
        car = Car(color, make, model)
        assert car.description == '{} {} {}'.format(color, make, model)

    def test_initial_state_is_stopped(self):
        """
        Ensure the a car's initial state is "stopped"
        """
        car = Car('Black', 'BMW', '335i')
        assert 'stopped' == car.state

    def test_state_after_start(self):
        """
        Ensure the car's state is "started" after using start method
        """
        car = Car('Black', 'BMW', '335i')
        car.start()
        assert 'started' == car.state

    def test_state_after_stop(self):
        """
        Ensure the car's state is "stopped" after using shutdown method
        """
        car = Car('Black', 'BMW', '335i')
        car.start()
        car.shutdown()
        assert 'stopped' == car.state

    def test_str_builtin(self):
        """
        Ensure the car evaluates to a string of
        "I am a <car color>, <car make>, <car model>."
        """
        color = 'white'
        make = 'Ford'
        model = 'Bronco'
        car = Car(color, make, model)
        assert str(car) == 'I am a {} {} {}.'.format(color, make, model)

    def test_color_requirement(self):
        """
        Ensure the car requires a color argument during instantiation
        """
        make = 'Ford'
        model = 'Mustang'
        with pytest.raises(TypeError):
            Car(make=make, model=model)

    def test_make_requirement(self):
        """
        Ensure the car requires a make argument during instantiation
        """
        color = 'black'
        model = 'Civicar'
        with pytest.raises(TypeError):
            Car(color=color, model=model)

    def test_model_requirement(self):
        """
        Ensure the car requires a model argument during instantiation
        """
        make = 'Porsche'
        color = 'silver'
        with pytest.raises(TypeError):
            Car(make=make, color=color)

    def test_state_read_only(self):
        """
        Ensure the car state attribute is read only and throws
        AttributeError if someone tries to assign a value directly
        """
        car = Car('Black', 'BMW', '335i')
        with pytest.raises(AttributeError):
            car.state = "started"

    def test_car_is_a_vehicle(self):
        """
        Ensure a car object is also an instance of BaseVehicle
        """
        car = Car('Black', 'BMW', '335i')
        assert isinstance(car, Car)
