# Copyright 2014 Stefan Winterfeldt <stefan.winterfeldt@bitz.it>
#                                  <stefan.winterfeldt@outlook.de>
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

"""This module contains the console message sink.

All message sink modules must implement the 'getInstance' method, returning
an instance of the message sink class that has been initialized with the
appropriate args dictionary.
"""
from messageSinks.abstractMessageSink import AbstractMessageSink
import libs.statusEnum as statusEnum


class ConsoleMessageSink(AbstractMessageSink):
    """A message sink that simply displays messages on the console.

    This message sink uses the following arguments:
        errorMessage - The message to display in case of an error status.
        failureMessage - The message to display in case of a failure status.
        successMessage - The message to display in case of a success status.
    """

    def __init__(self, args):
        self.errorMessage = args['errorMessage']
        self.failureMessage = args['failureMessage']
        self.successMessage = args['successMessage']

    def showStatus(self, status):
        if status == statusEnum.STATUS_ERROR:
            print(self.errorMessage)
        elif status == statusEnum.STATUS_FAILURE:
            print(self.failureMessage)
        elif status == statusEnum.STATUS_SUCCESS:
            print(self.successMessage)


def getInstance(args):
    return ConsoleMessageSink(args)