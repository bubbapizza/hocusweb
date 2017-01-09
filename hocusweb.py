#!/usr/bin/python

# This is an attempt to make a web-based keypad for entering the 2-factor 
# authentication of a wifi-based door controller. 
#
# Shawn Wilson
# Jan 2017

import cherrypy
import database
import os

### CONSTANTS ###
SQLITE_DB = "./database.db"

HTML_DOOR_OPEN = """
<!DOCTYPE html>
<html>

    <head>
        <title>Open Sesame</title>
    </head>

    <body>
       Door is open!!!<br/><br/>
       your IP is: {} <br/>
       your PIN code is: {}
    </body> 
</html>
"""

class authenticate(object):
    """This is the website for doing two-factor authentication using a PIN 
    code.  It assumes the IP address of the client is tied to the mac
    address of the user's device.  This is the 'something you have' part
    of two-factor authentication.  The pin code is the 'something you know'
    part."""

    def __init__(self):
        """Initialize the database for the website."""

        self.db = database.SQLite(SQLITE_DB)

    @cherrypy.expose
    def index(self):
        """The main page shows the keypad."""
        
        html = open("html/index.html").read()
        return html


    @cherrypy.expose
    def open(self, pin=""):
        """Validate a user based on IP address and PIN code, then open the
        door and show a message."""

        if len(pin) != 4:
            html = open("html/badpin.html").read()
            return html

        ip = cherrypy.request.remote.ip
        if True:
        #if self.db.validate_key_code(ip, pin):
            html = HTML_DOOR_OPEN.format(ip, pin)
            return html
        else:
            html = open("html/badpin.html").read()
            return html


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/html': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './html'
        }
    }
    cherrypy.quickstart(authenticate(), "/", conf)
    
