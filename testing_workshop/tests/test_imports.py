# tests.test_imports.py
# Test the imports for the motorsports library
#
# Author:     Allen Leis <allen.leis@georgetown.edu>
# Created:    Fri Sep 11 23:22:32 2015 -0400
# Adapted by: Rebecca Bilbro <rsb89@georgetown.edu>
# Updated on: Thu Mar 5 14:20:08 EST 2020
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: test_imports.py [] rsb89@georgetown.edu $

"""
Test imports and initialization for the motorsports library.
"""

##########################################################################
## Imports
##########################################################################

import pytest

##########################################################################
## Initialization Tests
##########################################################################


class TestImports():

    def test_import_motorsports(self):
        """
        Ensure the test suite can import the motorsports module
        """
        try:
            import motorsports
        except ImportError:
            self.fail("Was not able to import the motorsports")

    def test_import_buildings(self):
        """
        Ensure the test suite can import the buildings module
        """
        try:
            import motorsports.buildings
        except ImportError:
            self.fail("Was not able to import the motorsports")

    @pytest.mark.skip(reason="pending test code")
    def test_import_vehicles(self):
        """
        Ensure the test suite can import the vehicles module
        """
        pass
