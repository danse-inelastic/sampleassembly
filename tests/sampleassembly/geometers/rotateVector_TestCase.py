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


class TestCase(unittest.TestCase):
    
    
    def test(self):
        """
        sampleassembly.geometers.rotateVector.toMatrix
        """
        from sampleassembly.geometers.rotateVector import toMatrix
        for rx in np.arange(0,360,30.):
            for ry in np.arange(0, 360, 30.):
                for rz in np.arange(0, 360, 30.):
                    M1 = np.dot(
                        toMatrix( 0, 0, rz, unit='deg'),
                        np.dot(toMatrix( 0, ry, 0, unit='deg'),
                            toMatrix( rx, 0, 0, unit='deg') ),
                        )
                    M2 = toMatrix(rx, ry, rz, unit='deg')
                    np.testing.assert_array_almost_equal(M1, M2)
                    continue
                continue
            continue
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
__id__ = "$Id$"

# End of file 
