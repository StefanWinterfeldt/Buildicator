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

"""This module contains the RPI sound message sink.

All message sink modules must implement the 'getInstance' method, returning
an instance of the message sink class that has been initialized with the
appropriate args dictionary.
"""

from messageSinks.abstractMessageSink import AbstractMessageSink
import libs.statusEnum as statusEnum
import subprocess


class RPISoundMessageSink(AbstractMessageSink):
    """Plays the given sound when running on a Raspberry Pi.

    The sound is only played when the status changes from its previous value.
    This message sink uses the following arguments:
        errorSound - The sound file to play in case of an error status.
        failureSound - The sound file to play in case of a failure status.
        successSound - The sound file to play in case of a success status.
    """

    def __init__(self, args):
        self.errorSoundFilename = args['errorSound']
        self.failureSoundFilename = args['failureSound']
        self.successSoundFilename = args['successSound']
        self.lastStatus = None

    def playSound(self, soundFilename):
        subprocess.call(['aplay', soundFilename])

    def statusIsNew(self, status):
        return (self.lastStatus != None) and (status != self.lastStatus)

    def showStatus(self, status):
        if self.statusIsNew(status):
            if status == statusEnum.STATUS_ERROR:
                self.playSound(self.errorSoundFilename)
            elif status == statusEnum.STATUS_FAILURE:
                self.playSound(self.failureSoundFilename)
            elif status == statusEnum.STATUS_SUCCESS:
                self.playSound(self.successSoundFilename)
        self.lastStatus = status


def getInstance(args):
    return RPISoundMessageSink(args)