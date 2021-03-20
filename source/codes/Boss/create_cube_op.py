import bpy
from boss.ui_creator import *

def onEnterPress(caller):
    bpy.ops.mesh.primitive_cube_add(size=2)
    bpy.context.object.name = caller.value
    caller.op.quit()  # to quit after the button is clicked.


class CreateCubeOperator(Boss_OT_base_ui):
    """Create A Simple Cube"""
    bl_idname = "boss.create_cube"
    bl_label = "Create Cube"

    def ui_elements(self):
        op = self
        UICreator.deleteAllUi(op)  # to delete all existing ui
        btn_width, btn_height = 100, 40

        rr = UICreator.rr(op)  # region_rect(rr)

        rd = (
            rr.width / 2 - btn_width / 2,
            rr.height / 2 - btn_height / 2,
            btn_width,
            btn_height
        )
        UICreator.textField(
            op,
            rectData=rd,
            text='Cube',
            onEnterPress=onEnterPress
        )

def register():
    bpy.utils.register_class(CreateCubeOperator)

def unregister():
    bpy.utils.unregister_class(CreateCubeOperator)


if __name__ == "__main__":
    register()

# test call
# bpy.ops.boss.create_cube()
