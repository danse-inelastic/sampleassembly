#!/usr/bin/env python
#
#


def xyzfile2unitcell( filename ):
    from .xyzfile import read
    return read(filename)

def ciffile2unitcell(filename):
    from diffpy.Structure.Parsers import getParser
    p = getParser('cif')
    return p.parseFile(filename)

# End of file 
