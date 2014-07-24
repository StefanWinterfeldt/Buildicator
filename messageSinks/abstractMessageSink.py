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

"""Contains the abstract message sink class.
"""


class AbstractMessageSink():
    """The abstract base class of all message sinks.

    You could of course pass a message sink object to the manager that does not
    subclass this. It exists mainly to show that all message sinks should accept
    the 'args' parameter upon instantiation and implement a 'showStatus' method.
    """

    def __init__(self, args):
        raise NotImplementedError()

    def showStatus(self, status):
        raise NotImplementedError()