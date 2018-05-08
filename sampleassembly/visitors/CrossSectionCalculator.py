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


class CrossSectionCalculator:


    def __call__(self, scatterer, include_density=True):
        self.include_density = include_density
        return scatterer.identify(self)


    def onPowderSample(self, powder):
        # a powder sample must have a crystal phase
        phase = powder.phase
        assert phase.type == 'crystal'
        crystal = phase
        return self.onCrystal(crystal)


    def onCrystal(self, crystal):
        #unit cell
        unitcell = crystal.unitcell
        return self.onUnitCell( unitcell )
    

    def onUnitCell(self, unitcell):
        #atoms
        # atoms = unitcell.getAtoms()
        atoms = unitcell[:]
        #
        abs = sum( [ xs(atom, 'absorption') for atom in atoms ] )
        coh = sum( [ xs(atom, 'coherent') for atom in atoms ] )
        inc = sum( [ xs(atom, 'incoherent') for atom in atoms ] )
        ret = N.array( [abs, inc, coh] )

        import units
        barn = units.area.barn
        ret = ret*barn

        if not self.include_density:
            return ret
        
        #volumn of unit cell
        # v = volume( * unitcell.getCellVectors() )
        v = volume( * unitcell.lattice.base )
        A = units.length.angstrom
        unit = A**3
        ret = ret/(v*unit)
        
        return ret

    #end of CrossSectionCalculator


import periodictable
def xs(atom, type):
    elem = getattr(periodictable, atom.element)
    return getattr(elem.neutron, type)

def volume( a, b, c ):
    return N.dot( a, N.cross(b,c) )

import numpy as N


# version
__id__ = "$Id$"

# End of file 
