#!/usr/bin/env python
#
#

from pyre.xml.Node import Node
import urllib.request, urllib.parse, urllib.error


class ciffile(Node):

    tag = 'ciffile'

    def __init__(self, document, attributes):
        Node.__init__(self, document)
        return


    def notify(self, parent):
        return parent.onCIFfile( self.filename )


    def content(self, content):
        content = content.strip()
        if len(content)==0: return
        content = urllib.parse.unquote(content).strip()
        self.filename = content
        self.locator = self.document.locator
        return

    pass


# End of file 
