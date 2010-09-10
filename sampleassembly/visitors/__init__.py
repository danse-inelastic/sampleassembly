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


def cross_sections( scatterer, calculator = None, include_density = True):
    '''calculate cross-sections or cross-sections*density
    of the given scatterer
    
    inputs:
      scatterer: the scatterer object
      include_density: if true, include the density in the returned values
      calculator: the calculator

    return:
      absorption_cross_section (* rho)
      incoherent_scattering_cross_section (* rho)
      coherent_scattering_cross_section (* rho)

      where rho is the density.
    '''
    
    if calculator is None:
        from CrossSectionCalculator import CrossSectionCalculator
        calculator = CrossSectionCalculator()
        pass
    return calculator( scatterer, include_density=include_density )



# version
__id__ = "$Id$"

# End of file 
