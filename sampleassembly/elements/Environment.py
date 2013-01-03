#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from Element import Element
from _journal import debug
from pyre.units.temperature import K


class Environment( Element ):

    allowed_item_types = [
        ]

    class Attributes(Element.Attributes):

        import Attribute
        temperature = Attribute.dimensional('temperature', default=300*K)
        pass
        

    def __init__( self, **attributes):
        Element.__init__(self, 'sample-environment', **attributes)
        return
    
    
    def identify( self, visitor):
        return visitor.onEnvironment( self )

    pass # end of Environment



# version
__id__ = "$Id$"

# End of file
