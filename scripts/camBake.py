#2017 Julián Herrera
#camBake - select a camera, run script. Places baked clone at the project root.

import pymel.core as pm

def getSelection():
    selection = pm.ls(sl=True)
    if len(selection) == 1: 
        shapes = pm.listRelatives( selection[0], shapes=True )
        if pm.nodeType(shapes[0]) == 'camera':
            bakeCamToWorld(selection[0])

def bakeCamToWorld(camera):
    bakedCam = pm.duplicate(camera,name=camera.name()+'_publish',rc=True, rr=True, ic=True)
    children = pm.listRelatives(bakedCam,c=True,pa=True)[1:]
    for c in children:
        pm.delete(c)
    parent = pm.listRelatives(camera,parent=True)
    if len(parent) != 0:
        pm.parent(bakedCam,w=True)

    pm.parentConstraint(camera,bakedCam,mo=False)
    start = pm.playbackOptions(q=True,minTime=True)
    end = pm.playbackOptions(q=True,maxTime=True)
    
    pm.bakeResults(bakedCam, t=(start,end))
    pm.delete(bakedCam[0] + '*Constraint*')
    
getSelection()
