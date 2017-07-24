import maya.cmds as cmds
from functools import partial

class selectionSetGUI(object):
    def __init__(self):
        return None

    def select(self, set, *args):
        print set
        cmds.select(set)
        
    def populate(self):
        setArray = []
        setObjects = cmds.ls(exactType="objectSet")
        for set in setObjects:
            if cmds.sets(set, q=True, text=True) == "gCharacterSet":
                setArray.append(set)
        for set in setArray:
            cmds.button(label=set, parent=self.mainLayout, command=partial(self.select, set))
            
    def show(self):
        self.create()
        self.populate()

    def create(self):
        self.winID = 'Selection Set Picker'
        if cmds.window(self.winID, query=True, exists=True):
            cmds.deleteUI(self.winID)
        self.window = cmds.window(self.winID, rtf=True, title="Selection Set Picker")
        self.mainLayout = cmds.columnLayout(adj=True)        
        cmds.showWindow(self.window)

ssG = selectionSetGUI()
ssG.show()
