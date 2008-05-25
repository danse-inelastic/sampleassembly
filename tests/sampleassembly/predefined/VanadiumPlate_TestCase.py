#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest


from unittestX import TestCase
class VanadiumPlate_TestCase(TestCase):


    def test0(self):
        """
        sampleassembly.predefined.VanadiumPlate
        """
        from sampleassembly.predefined.VanadiumPlate import VanadiumPlate
        vp = VanadiumPlate( )

        from sampleassembly.geometers import coordinateSystem
        vp.geometer.changeRequestCoordinateSystem( coordinateSystem(
            'InstrumentScientist' ) )
        orientation = vp.getSampleOrientation()
        self.assertAlmostEqual( orientation[0]/degree, 0 )
        self.assertAlmostEqual( orientation[1]/degree, 0 )
        self.assertAlmostEqual( orientation[2]/degree, 135 )
        return

    pass # end of VanadiumPlate_TestCase


import sampleassembly.units as units
degree = units.angle.degree


import unittest

def pysuite():
    suite1 = unittest.makeSuite(VanadiumPlate_TestCase)
    return unittest.TestSuite( (suite1,) )



def main():
    import journal
    from instrument.elements import debug
    debug.activate()
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id$"

# End of file 
