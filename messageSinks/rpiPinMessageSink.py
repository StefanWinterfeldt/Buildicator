#Copyright 2014 Stefan Winterfeldt <stefan.winterfeldt@bitz.it>
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

"""This module contains the RPI pin message sink.

All message sink modules must implement the 'getInstance' method, returning
an instance of the message sink class that has been initialized with the
appropriate args dictionary.
"""
from messageSinks.abstractMessageSink import AbstractMessageSink
import os.path
import libs.statusEnum as statusEnum
import libs.pins as pins

class RPIPinMessageSink (AbstractMessageSink):
	"""Switches the given pins on or off when running on a Raspberry Pi.
	
	This message sink uses the following arguments:
		errorPin - The pin to power in case of an error status.
		failurePin - The pin to power in case of a failure status.
		successPin - The pin to power in case of a success status.
	"""
	def __init__ (self, args):
		self.errorPin = args['errorPin']
		self.failurePin = args['failurePin']
		self.successPin = args['successPin']
		self.initializePins ()
		
	def initializePin (self, pin):
		if pins.pinExists (pin):
			pins.unexport (pin)
		pins.export (pin)
		pins.setDirectionOut (pin)
		
	def initializePins (self):
		self.initializePin (self.errorPin)
		self.initializePin (self.failurePin)
		self.initializePin (self.successPin)
		
	def setAllPinsOff (self):
		pins.setOff (self.errorPin)
		pins.setOff (self.failurePin)
		pins.setOff (self.successPin)
		
	def showStatus (self, status):
		self.setAllPinsOff ()
		if status == statusEnum.STATUS_ERROR:
			pins.setOn (self.errorPin)
		elif status == statusEnum.STATUS_FAILURE:
			pins.setOn (self.failurePin)
		elif status == statusEnum.STATUS_SUCCESS:
			pins.setOn (self.successPin)
			
def getInstance (args):
	return RPIPinMessageSink (args)