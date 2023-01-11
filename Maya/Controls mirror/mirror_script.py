import maya.cmds as cmds
from functools import partial

def mirror_contrl(way, *args):
    
    
    curSel = cmds.ls(sl=True)
    for obj in curSel:
        cmds.select(obj)
        cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0)
        
    print (curSel)
    for obj in curSel:
        rotation = []
        print(len(curSel))
        pos = cmds.xform(obj, q=1, rp=True, ws=True)
        current_pos = cmds.xform(obj, q=1, t=True, ws=True)
        print ("pos", pos)
        print("current_pos ", current_pos)
        
        cmds.duplicate(obj)
        
        if current_pos != pos:
            print('oops')
            cmds.setAttr(obj+".translateX", current_pos[0] - pos[0])
            cmds.setAttr(obj+".translateY", current_pos[1] - pos[1])
            cmds.setAttr(obj+".translateZ", current_pos[2] - pos[2])
            cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0)
        
        
        rotation.append(cmds.getAttr("%s.rotateX" % obj))
        rotation.append(cmds.getAttr("%s.rotateY" % obj))
        rotation.append(cmds.getAttr("%s.rotateZ" % obj))
        cmds.select(obj)
        print('rotation', rotation)
        if way == 1:  #XY
            cmds.setAttr(obj+".translateX", pos[0])
            cmds.setAttr(obj+".translateY", pos[1])
            cmds.setAttr(obj+".translateZ", pos[2]*(-1))
            cmds.rotate(180, 180, 0, relative=True, componentSpace=True)
            
        elif way == 2:  #YZ
            cmds.setAttr(obj+".translateX", pos[0]*(-1))
            cmds.setAttr(obj+".translateY", pos[1])
            cmds.setAttr(obj+".translateZ", pos[2])
            cmds.rotate(0, 180, 180, relative=True, componentSpace=True)
                      
        elif way == 3:  #XZ
            cmds.setAttr(obj+".translateX", pos[0])
            cmds.setAttr(obj+".translateY", pos[1]*(-1))
            cmds.setAttr(obj+".translateZ", pos[2])
            cmds.rotate(180, 0, 180, relative=True, componentSpace=True)
            
            
        cmds.makeIdentity(obj, apply=True, t=1, r=1, s=1, n=0)
        
        

def extrWindow():
    """Creates the user interface UI for the user input of the extrusion scale and height"""
    windowID = "superExtrWindow"

    if cmds.window(windowID, exists=True):
        cmds.deleteUI(windowID)

    cmds.window(windowID, title="Control mirror", sizeable=True, widthHeight=(20, 30))
    cmds.rowColumnLayout(numberOfColumns=4, columnWidth=[(1,100),(2,100), (3, 100), (4,100)], columnOffset=[1,"right",3])

    cmds.text(label="Mirror axis:")
    way1 = 1
    way2 = 2
    way3 = 3

    cmds.button(label="XY", command=partial(mirror_contrl, way1))
    cmds.button(label="YZ", command=partial(mirror_contrl, way2))
    cmds.button(label="XZ", command=partial(mirror_contrl, way3))
    cmds.showWindow(windowID)

extrWindow()
