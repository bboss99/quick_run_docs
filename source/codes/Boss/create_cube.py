import bpy
from boss.ui_creator import UICreator

def onEnterPress(caller):
    bpy.ops.mesh.primitive_cube_add(size=2)
    bpy.context.object.name = caller.value
    caller.op.quit()  # to quit after the button is clicked.


def ui_elements(op):
    UICreator.deleteAllUi(op)  # to delete all existing ui
    btn_width, btn_height = 100, 40

    rr = UICreator.rr(op)  # region_rect(rr)

    rd = (
        rr.width/2 - btn_width/2,
        rr.height/2 - btn_height/2,
        btn_width,
        btn_height
    )
    UICreator.textField(
        op,
        rectData=rd,
        text='Cube',
        onEnterPress=onEnterPress
    )
