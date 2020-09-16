
class CoordinateSystem:


    def __init__(self, name, description = "",
                 neutronBeamDirection = None, gravityDirection = None):
        '''CoordinateSystem( name, description,
  neutronBeamDirection, gravityDirection)
        
  - neutronBeamDirection: direction vector of neutron beam.
    It must be a unit vector.
  - gravityDirection: direction vector of gravity.
    It must be a unit vector too.
    '''
        self.name = name
        self.description = description
        self.neutronBeamDirection = neutronBeamDirection
        self.gravityDirection = gravityDirection
        return

    pass # end of CoordinateSystem


McStasCSDesc = """
z: downstream neutron beam from moderator
y: vertical up

rotation:
  (rx, ry, rz) --> rotate rx by axis x, then ry by axis y, then rz by axis z
"""
McStasCS = CoordinateSystem(
    'McStas',  McStasCSDesc, (0,0,1), (0,-1,0) )



ISCSDesc = '''
x: downstream tneutron beam from moderator
z: vertical up

orientation is (rx, ry, rz): three rotations, one each about fixed axes
        parallel to the instrument x, y, and z axes.
'''
InstrumentScientistCS = CoordinateSystem(
    'InstrumentScientist', ISCSDesc, (1,0,0), (0,0,-1) )


def InstrumentScientistCS2McStasCS( position, orientation ):
    x,y,z = position
    positionMcStas = y,z,x
    rx, ry, rz = orientation
    from .rotateVector import toMatrix, toAngles, dot
    import numpy as np
    M = toMatrix(rx,ry,rz, unit='deg')
    S = [[0,0,1.],
         [1,0,0],
         [0,1,0]]
    S = np.array(S)
    M1 = dot(S.T, dot(M, S))
    from .mcstasRotations import toAngles
    rotationMcStas = toAngles(M1.T, unit='deg' )
    return positionMcStas, rotationMcStas


def fitCoordinateSystem( posori, coord_sys, new_coord_sys):
    if coord_sys == new_coord_sys: return posori
    name = "%sCS2%sCS" % (coord_sys.name, new_coord_sys.name)
    try:
        converter = eval( name )
    except:
        raise NotImplementedError("Cannot find converter %s" % name)
    pos, ori = posori
    return converter(pos, ori) 


def relative2absoluteMcStas( relative_posori, reference_posori):
    from numpy import dot, array
    from .mcstasRotations import toMatrix, toAngles
    
    rel_pos, rel_ori = relative_posori
    ref_pos, ref_ori = reference_posori
    parentM = toMatrix( ref_ori, unit='deg')
    m = toMatrix( rel_ori, unit = 'deg')
    absM = dot( m , parentM )
    absRots = toAngles( absM, unit = 'deg' )

    from .rotateVector import toMatrix
    ref_pos = array(ref_pos)
    absPos = ref_pos + dot( toMatrix( ref_ori, unit='deg' ), rel_pos )
    return absPos, absRots


relative2absolute = {
    McStasCS: relative2absoluteMcStas,
    InstrumentScientistCS: relative2absoluteMcStas,
    }
    


def coordinateSystem( name ):
    ret = eval( '%sCS' % name )
    assert ret.name == name
    return ret


