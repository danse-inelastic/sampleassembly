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


from ElementContainer import ElementContainer, typeFromName
from _journal import debug


#A sample assembly is a component (element) in a neutron instrument.
#We call that component "sample" in the instrument package.
#In order for a sample assembly to be an element in instruments,
#we need it to be a subclass of the "Sample" class of instrument
#package.
#Is there a better way to make this statement?
from instrument.elements.Sample import Sample as base

class SampleAssembly( ElementContainer, base ):

    '''Sample assembly

    A sample assembly represents everything installed on the sample
    position of an instrument. It is a container of sample, sample holder,
    and maybe furnace, and more.

    A sample assembly is assumed to be installed at a fixed position
    and orientation in the instrument. That position and orientation
    is defined by convention, and is fixed for an instrument. 
    For an experiment done in that instrument, we may want to
    rotate or move sample or other things in the assembly, and that
    should be done with the geometer associated with this sample
    assembly.
    '''

    allowed_item_types = [
        'PowderSample',
        'Environment',
        ]    

    class Attributes(ElementContainer.Attributes):

        import Attribute
        max_multiplescattering_loops_among_scatterers = Attribute.int(
            'max_multiplescattering_loops_among_scatterers', 
            default = 5)
        max_multiplescattering_loops_interactM_path1 = Attribute.int(
            'max_multiplescattering_loops_interactM_path1',
            default = 2)
        min_neutron_probability = Attribute.float(
            'min_neutron_probability',
            default = 0.)
        pass
        

    def __init__( self, name, shape = None, **attributes):
        """ Sample assembly ctor
        """
        #this implementation is a bit weird.
        #should we inherit from instrument.Sample only?
        base.__init__(
            self, name, shape = shape, **attributes)
        ElementContainer.__init__(
            self, name, shape = shape, **attributes)
        self._sample = None
        return


    def identify( self, visitor):
        return visitor.onSampleAssembly( self)


    def addSample(self, sample):
        '''add sample to this assembly
        '''
        if self._sample:
            raise RuntimeError, "there is already a sample"
        self._sample = sample
        self.addElement( sample )
        return


    def getOrientation(self, scatterer):
        geometer = self._getGeometer()
        return geometer.orientation( scatterer )


    def getSampleOrientation(self):
        return self.getOrientation( self.getSample() )


    def getSample(self): return self._sample


    def getEnvironment(self):
        from .Environment import Environment
        for elem in self.elements():
            if isinstance(elem, Environment):
                return elem
        return
        

    def _getGeometer(self):
        try: return self.geometer
        except AttributeError:
            raise RuntimeError, "sample assembly needs a geometer"
        
    pass # end of SampleAssembly




# version
__id__ = "$Id: SampleAssembly.py 487 2005-06-22 22:52:09Z tim $"

# End of file
