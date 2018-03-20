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


from numpy import array
from pyre.units.length import m


import unittest


from unittestX import TestCase as base
class TestCase(base):


    def test0(self):
        """
        sampleassembly.saxml.parser
        """
        from sampleassembly.saxml import parse_file
        sampleassembly = parse_file( 'Ni.xml' )
        geometer = sampleassembly.local_geometer
        Ni_powder = sampleassembly.elements()[0]
        shape = Ni_powder.shape()
        assert shape.__class__.__name__ == 'Union', len(shape.shapes)==3
        phase = Ni_powder.phase
        self.assertEqual( phase.__class__.__name__, 'Crystal' )
        self.assertEqual( phase.chemical_formula, 'Ni' )
        crystal = phase
        unitcell = crystal.unitcell
        print unitcell
        return


    def test1(self):
        """
        sampleassembly.saxml.parser: with sample environment
        """
        from sampleassembly.saxml import parse_file
        sampleassembly = parse_file( 'Ni-withenviron.xml' )
        env = sampleassembly.getEnvironment()
        print env
        print env.attributes.temperature
        # print type(env.attributes.temperature)
        from pyre.units import temperature as T
        print env.attributes.temperature/T.K
        print env.temperature()
        return


    pass # end of TestCase


import unittest

def pysuite():
    suite1 = unittest.makeSuite(TestCase)
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
__id__ = "$Id: parser_TestCase.py 1264 2007-06-04 17:56:50Z linjiao $"

# End of file 
