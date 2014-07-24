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

"""Contains the project class.
"""


class Project():
    """Uses a connector to get a status and message sinks to show it.

    A project can only have one connector to get information about its current
    status. This status can however be show on multiple different message sinks.
    """

    def __init__(self, connector, messageSinks):
        self.connector = connector
        self.messageSinks = messageSinks

    def refreshStatus(self):
        status = self.connector.getStatus()
        for sink in self.messageSinks:
            sink.showStatus(status)