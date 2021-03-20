import bpy
from boss.ui_creator import *

def onClick(caller):
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    caller.op.quit()


class CreateCubeOperator(Boss_OT_base_ui):
    """Create A Simple Cube"""
    bl_idname = "boss.create_cube"
    bl_label = "Create Cube"
    
    def ui_elements(self):
        op = self
        UICreator.button(
            op,
            rectData=RectData(0, 0, 100, 40),
            text='text',
            buttonData=onClick,
        )        
        

def register():
    bpy.utils.register_class(CreateCubeOperator)

def unregister():
    bpy.utils.unregister_class(CreateCubeOperator)


if __name__ == "__main__":
    register()

# test call
# bpy.ops.boss.create_cube()

