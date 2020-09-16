#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from .AbstractNode import AbstractNodeBase, debug


class Environment(AbstractNodeBase):


    tag = "Environment"
    
    from sampleassembly.elements.Environment import Environment as ElementFactory

    def __init__(self, document, attributes):
        super(Environment, self).__init__(document)
        # new element
        self.element = self.ElementFactory(**attributes)
        return


    pass # end of Environment


# version
__id__ = "$Id$"

# End of file 
