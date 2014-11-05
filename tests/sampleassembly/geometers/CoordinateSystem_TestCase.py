#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2007-2014 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import unittest, numpy as np


from unittest import TestCase
class TestCase(unittest.TestCase):


    def test(self):
        """sampleassembly.geometers.CoordinateSystem.InstrumentScientistCS2McStasCS
        """
        from sampleassembly.geometers.CoordinateSystem import InstrumentScientistCS2McStasCS as I2MC
        v, r = I2MC( (1,0,0), (0,0,30) )
        np.testing.assert_array_almost_equal(v, (0,0,1))
        np.testing.assert_array_almost_equal(r, (0,30,0))
        
        v, r = I2MC( (1,0,0), (-135,0,125.26438968275465) )
        np.testing.assert_array_almost_equal(r, [-180, 54.735610317245346, 45])
        return


import unittest

def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )



def main():
    import journal
    pytests = pysuite()
    alltests = unittest.TestSuite( (pytests, ) )
    unittest.TextTestRunner(verbosity=2).run(alltests)
    return


if __name__ == '__main__': main()
    

# version
__id__ = "$Id: renderer_TestCase.py 1264 2007-06-04 17:56:50Z linjiao $"

# End of file 
