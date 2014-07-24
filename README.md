Buildicator
===========

Buildicator is a build indication tool that uses connectors (e.g. a REST interface) to query the state of a build and 
message sinks (e.g. an LED connected to a Raspberry Pi) to visualize that state. 

How do I use it?
----------------

Run "python3 buildicate.py -c config-skeleton.json" for an example that will generate random build states via the dummy
connector and print them to console via the console message sink. This is the simplest configuration and should work on 
most platforms. Play around with the skeleton config and take a look at "config-example.json" as well as the docstrings
of the other currently existing connectors and message sinks. If you own a Raspberry Pi and your project uses TeamCity
you can already use Buildicator to create your own build light.

How do I extend it?
-------------------

New connectors or message sinks need to do 4 things (always see other connectors/message sinks for reference):

- They need to reside in the connectors or messageSinks folder respectively
- They need to override the methods in their respective abstract base classes
- They need to define a getInstance method in their file
- Their files need to have the "Connector" or "MessageSink" suffix.

If these conditions are met you only need to add them to the active config file by name and supply the needed arguments.
Let's imagine you just wrote a message sink (contained in the file mailMessageSink.py) that sends emails with an error, 
failure or success message to a given address. The configuration could look like this:

    "messageSinks" : [
        {
            "name" : "mail",
            "args" : {
                "errorMessage" : "state of build could not be determined",
                "failureMessage" : "the build failed",
                "successMessage" : "the build succeeded",
                "receiver" : "project.manager@yourCompany.com"
        }
    ]
