#!

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

"""Builds projects as specified in the config and refreshes them periodically.

This script instantiates a list of project objects with their corresponding
connectors and message sinks as defined in the configuration file. The projects
are then refreshed every n seconds according to the 'interval' parameter in
the configuration. The location of the configuration file defaults to 
'config.json' but can be given as a command line parameter with the -c option.
"""

import argparse
import importlib
import json
from libs.project import Project
import time


def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', help='configuration file path', type=str, default='config.json')
    return parser.parse_args()


def getConnector(connectorConfiguration):
    return getObjectFromConfiguration(connectorConfiguration, 'Connector', 'connectors')


def getDynamicObject(moduleName, args, location=''):
    if location != '':
        module = importlib.import_module(location + '.' + moduleName)
    else:
        module = importlib.import_module(moduleName)
    return module.getInstance(args)


def getMessageSink(messageSinkConfiguration):
    return getObjectFromConfiguration(messageSinkConfiguration, 'MessageSink', 'messageSinks')


def getMessageSinks(messageSinkConfigurations):
    messageSinks = []
    for messageSinkConfiguration in messageSinkConfigurations:
        messageSinks.append(getMessageSink(messageSinkConfiguration))
    return messageSinks


def getObjectFromConfiguration(configuration, objectName, location=''):
    return getDynamicObject(configuration['name'] + objectName, configuration['args'], location)


def loadConfig(path):
    return json.load(open(path))


def initializeProject(projectConfiguration):
    connector = getConnector(projectConfiguration['connector'])
    messageSinks = getMessageSinks(projectConfiguration['messageSinks'])
    return Project(connector, messageSinks)


def initializeProjects(configuration):
    projects = []
    for projectConfiguration in configuration['projects']:
        projects.append(initializeProject(projectConfiguration))
    return projects


def refreshProjectsPeriodically(projects, interval):
    while True:
        for project in projects:
            project.refreshStatus()
        time.sleep(interval)


def main():
    arguments = getArguments()
    configuration = loadConfig(arguments.c)
    projects = initializeProjects(configuration)
    refreshProjectsPeriodically(projects, configuration['interval'])


if __name__ == '__main__':
    main()

