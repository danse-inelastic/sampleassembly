#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from pyre.xml.Node import Node


class Shape(Node):


    tag = "Shape"
    
     
    def __init__(self, document, attributes):
        Node.__init__(self, document)
        return


    def notify(self, parent):
        #parent is a xml node. parent.element is a sampleassembly element
        #that this shape should be attached to
        target = parent.element
        target.setShape( self._shape )
        return 


    def on_(self, sth):
        self._shape = sth
        return

    onUnion = on_
    onSphere = onCylinder = onBlock = onPyramid = onCone = on_
    onSphereShell = onHollowCylinder = on_

    onRotation = onTranslation = onDilation = on_
    onUnion = onIntersection = onDifference = on_

    pass # end of Shape
    

# End of file 
