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


def sampleassembly(*args, **kwds):
    '''sampleassembly( name, shape ) --> new sample assembly
    '''
    from SampleAssembly import SampleAssembly
    return SampleAssembly( *args, **kwds )


def powdersample( *args, **kwds ):
    '''powdersample( name, shape )'''
    from PowderSample import PowderSample
    return PowderSample( *args, **kwds )


def crystal(*args, **kwds):
    from Crystal import Crystal
    return Crystal(*args, **kwds)


def atom( *args, **kwds ):
    """create an atom
    
    atom( 26, 57 )
    atom( 26 )
    atom( 'Fe' )
    atom( 'Fe', 57 )
    """
    from matter import Atom
    return Atom(*args, **kwds )


# def unitcell( *args, **kwds ):
def unitcell(cellvectors, atoms, positions):
    '''
    Fe = atom( symbol='Fe', mass = 57)
    Al = atom( symbol='Al')
    atoms = Fe, Al
    positions = (0,0,0), (0.5,0.5,0.5) 
    cellvectors = [ (1,0,0), (0,1,0), (0,0,1) ]
    uc = unitcell( cellvectors, atoms, positions )
    '''
    # from crystal.UnitCell import create_unitcell
    from matter.Structure import Structure
    from matter.Lattice import Lattice
    base = cellvectors
    lattice = Lattice(base=base)
    atomlist = [
        atom(a, xyz=pos)
        for a, pos in zip(atoms, positions)
        ]
    return Structure(atoms, lattice)


# version
__id__ = "$Id$"

# End of file 
