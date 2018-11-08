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


from pyre.xml.Document import Document as DocumentNode


class Document(DocumentNode):


    tags = [
        "SampleAssembly",
        'Environment',
        'PowderSample',

        'Phase',
        'ChemicalFormula',
        'xyzfile', 'ciffile',

        'LocalGeometer',
        'Register',
        'GlobalGeometer',

        'Shape',
        'Cylinder', 'Block', 'Sphere', 'Pyramid', 'Cone',
        'HollowCylinder', 'SphereShell',

        'Angle', 'Axis', 'Vector',
        'Rotation', 'Translation', 'Dilation',
        'Union', 'Intersection', 'Difference',
        ]


    def onSampleAssembly(self, sampleassembly):
        self.document = sampleassembly
        return


# version
__id__ = "$Id: Document.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
