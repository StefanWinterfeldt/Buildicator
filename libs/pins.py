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

"""A VERY light interface to the gpio pins on a Raspberry Pi.

This module contains a few functions that are basically just short-cuts to the
file system interface of the gpio pins on a Raspberry Pi.
"""

import os.path


def export(pin):
    f = open('/sys/class/gpio/export', 'w')
    f.write(str(pin))
    f.close()


def pinExists(pin):
    return os.path.isdir('/sys/class/gpio/gpio' + str(pin))


def setDirectionOut(pin):
    f = open('/sys/class/gpio/gpio' + str(pin) + '/direction', 'w')
    f.write('out')
    f.close()


def setOff(pin):
    f = open('/sys/class/gpio/gpio' + str(pin) + '/value', 'w')
    f.write('0')
    f.close()


def setOn(pin):
    f = open('/sys/class/gpio/gpio' + str(pin) + '/value', 'w')
    f.write('1')
    f.close()


def unexport(pin):
    f = open('/sys/class/gpio/unexport', 'w')
    f.write(str(pin))
    f.close()