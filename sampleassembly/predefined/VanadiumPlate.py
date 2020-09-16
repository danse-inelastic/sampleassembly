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


from . import units
mm = units.length.mm
cm = units.length.cm
degree = units.angle.degree


from .SampleAssembly import SampleAssembly as base

class VanadiumPlate(base):


    def __init__(self, name = 'vanadiumPlate', 
                 width = None, height = None, thickness = None,
                 darkAngle = None):
        '''create a vanadium plate sample
        
        all inputs must have units attached
        '''
        self.name = name
        if width is None: width = 6*cm
        if height is None: height = 10*cm
        if thickness is None: thickness = 2*mm
        if darkAngle is None: darkAngle = 135 * degree
        
        self.width = width
        self.height = height
        self.thickness = thickness
        self.darkAngle = darkAngle

        from . import shapes
        plate = shapes.plate( width, height, thickness )
        from sampleassembly.elements import powdersample
        #should not we have crystalline info here?
        sample = powdersample( name, shape = plate)
        
        base.__init__(self, name, shape = plate)
        self.addSample( sample )

        #set up geometer
        from sampleassembly.geometers import geometer
        geometer  = geometer(self, registry_coordinate_system = 'InstrumentScientist')
        geometer.register( sample, (0,0,0), (0*degree,0*degree,darkAngle) )
        self.geometer = geometer
        return


    def dimensions(self): return self.width, self.height, self.thickness


    def setDarkAngle(self, darkAngle):
        self.darkAngle = darkAngle
        self.geometer.reregister( self.getSample(), (0,0,0), (0*degree,0*degree,darkAngle) )
        return
    


# version
__id__ = "$Id$"

# End of file 
