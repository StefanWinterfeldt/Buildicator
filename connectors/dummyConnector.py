# Copyright 2014 Stefan Winterfeldt <stefan.winterfeldt@bitz.it>
#                                   <stefan.winterfeldt@outlook.de
#                BITZ GmbH          <info@bitz.it>
#
#This file is part of Buildicator.
#
#Buildicator is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#Buildicator is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with Buildicator.  If not, see <http://www.gnu.org/licenses/>.

"""This module contains the dummy connector.

All connector modules must implement the 'getInstance' method, returning an 
instance of the connector class that has been initialized with the appropriate 
args dictionary.
"""

from connectors.abstractConnector import AbstractConnector
import random
import libs.statusEnum as statusEnum


class DummyConnector(AbstractConnector):
    """A connector that simply returns a status at random.

    This connector is useful for testing message sinks or the device it is
    running on. It does not connect to anything, therefore it does not use any
    arguments.
    """

    def __init__(self, args):
        pass

    def getStatus(self):
        return random.choice([statusEnum.STATUS_ERROR, statusEnum.STATUS_FAILURE, statusEnum.STATUS_SUCCESS])


def getInstance(args):
    return DummyConnector(args)