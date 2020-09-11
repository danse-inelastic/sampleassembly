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

from pyre.xml.Node import Node


class Phase(Node):

    tag = 'Phase'

    def __init__(self, document, attributes):
        Node.__init__(self, document)

        # convert to dictionary
        attrs = {}
        for k,v in attributes.items(): attrs[str(k)] = v

        type = attrs['type']
        from sampleassembly.elements import phases
        factory = getattr(phases, type )
        self.element = factory()
        return


    def notify(self, parent):
        return self.element.identify( parent )


    def onChemicalFormula(self, formula ):
        self.element.chemical_formula = formula
        return


    def onXYZfile(self, xyzfile):
        from sampleassembly.crystal.ioutils import xyzfile2unitcell
        try:
            self.element.unitcell = xyzfile2unitcell( xyzfile )
        except:
            import traceback
            tb = traceback.format_exc()
            marker = '*'*60
            msg = "Unable to parse xyz file %s. traceback:\n%s\n%s\n%s" % (
                xyzfile, marker, tb, marker)
            raise RuntimeError(msg)
        return


    def onCIFfile(self, ciffile):
        from sampleassembly.crystal.ioutils import ciffile2unitcell
        try:
            self.element.unitcell = ciffile2unitcell( ciffile )
        except:
            import traceback
            tb = traceback.format_exc()
            marker = '*'*60
            msg = "Unable to parse cif file %s. traceback:\n%s\n%s\n%s" % (
                ciffile, marker, tb, marker)
            raise RuntimeError(msg)
        return


    pass # end of Phase



# version
__id__ = "$Id$"

# End of file 
