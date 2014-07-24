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

"""This module contains the TeamCity REST v8 connector.

All connector modules must implement the 'getInstance' method, returning an 
instance of the connector class that has been initialized with the appropriate 
args dictionary.
"""

from connectors.abstractConnector import AbstractConnector
import base64
import json
import libs.statusEnum as statusEnum
import urllib.error
import urllib.request


class TeamCityREST8Connector(AbstractConnector):
    """A connector that queries a TeamCity server for a project's status.

    This connector will use the REST API provided by TeamCity 8.x to query a
    given project's status. If all builds in the given project are green,
    success will be returned. If at least one build is red, failure will be
    returned. If an error is encountered in the process, error will be returned.
    As a user account is usually needed to access the details of a project, it
    is advisable to create an account that has viewing privileges only.
    This connector uses the following arguments:
        url - The url of the TeamCity server, i.e. 'http://teamcity.example.com'
        projectName - The name/id of the project to be monitored
        userName - The user name of the account to be used for viewing
        password - The password of the account to be used for viewing
    """

    def __init__(self, args):
        self.url = args["url"]
        self.projectName = args["projectName"]
        self.userName = args["userName"]
        self.password = args["password"]

    def allBuildsAreSuccessful(self, referencesToBuildTypes):
        allBuildsSuccessful = True
        for reference in referencesToBuildTypes:
            buildTypeResponse = self.getJSONFromUrl(self.url + '/' + reference)
            if not buildTypeResponse['paused']:
                buildsResponse = self.getJSONFromUrl(self.url + '/' + reference + '/builds')
                allBuildsSuccessful &= (buildsResponse['build'][0]['status'] == 'SUCCESS')
        return allBuildsSuccessful

    def getBase64AuthString(self):
        return base64.b64encode(bytes(self.userName + ':' + self.password, encoding='UTF-8'))

    def getJSONFromUrl(self, url):
        req = urllib.request.Request(url)
        req.add_header('Authorization', self.getBase64AuthString())
        req.add_header('Accept', 'application/json')
        r = urllib.request.urlopen(req)
        decoder = json.JSONDecoder()
        return decoder.decode(str(r.read(), encoding='UTF-8'))

    def getReferencesToBuildTypesInProject(self):
        referencesToBuildTypes = []
        jsonResponse = self.getJSONFromUrl(self.url + '/httpAuth/app/rest/projects/id:' + self.projectName + '/')
        for buildType in jsonResponse['buildTypes']['buildType']:
            referencesToBuildTypes.append(buildType['href'])
        return referencesToBuildTypes

    def getStatus(self):
        try:
            referencesToBuildTypes = self.getReferencesToBuildTypesInProject()
            if self.allBuildsAreSuccessful(referencesToBuildTypes):
                return statusEnum.STATUS_SUCCESS
            else:
                return statusEnum.STATUS_FAILURE
        except (urllib.error.HTTPError, urllib.error.URLError, ValueError):
            return statusEnum.STATUS_ERROR


def getInstance(args):
    return TeamCityREST8Connector(args)