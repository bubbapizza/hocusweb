#!/usr/bin/python

# This is an attempt to make a web-based keypad for entering the 2-factor 
# authentication of a wifi-based door controller. 
#
# Shawn Wilson
# Jan 2017

import cherrypy

### CONSTANTS ###

class authenticate(object):

    @cherrypy.expose
    def index(self):
        """The main page shows the keypad."""
        
        html = open("index.html").read()
        return html


    @cherrypy.expose
    def open(self, pinCode=""):
        """Validate a user based on IP address and PIN code, then open the
        door and show a message."""

        if len(pinCode) != 4:
            html = open("badpin.html").read()
            return html
        ip = cherrypy.request.remote.ip


    
    
