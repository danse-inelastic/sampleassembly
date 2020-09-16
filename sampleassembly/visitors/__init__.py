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


def compute_absorption_and_scattering_coeffs(scatterer):
    '''calculate absorption and scattering coefficients
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
    
    from .CrossSectionCalculator import CrossSectionCalculator
    calculator = CrossSectionCalculator()
    return calculator(scatterer, include_density=True)


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
    if include_density:
        import warnings
        msg = "To compute absorption and scattering coefficients, use method"\
            " 'compute_absorption_and_scattering_coeffs'."
        warnings.warn(msg, DeprecationWarning)
        return compute_absorption_and_scattering_coeffs(scatterer)

    if not calculator:
        from .CrossSectionCalculator import CrossSectionCalculator
        calculator = CrossSectionCalculator()
    return calculator(scatterer, include_density=False)


# version
__id__ = "$Id$"

# End of file 
