import bpy
from boss.ui_creator import *

def onClick(caller:Button):
    print('button is clicked')
    caller.op.quit()  # to quit after the button is clicked.


def ui_elements(op:Boss_OT_base_ui):
    # op.uip.deleteAllUi() # to delete all existing ui
    UICreator.deleteAllUi(op)
    btn_width, btn_height = 100, 40

    rr = op.uip.region_rect

    rd = RectData(
        rr.width/2 - btn_width/2,
        rr.height/2 - btn_height/2,
        btn_width,
        btn_height
    )

    UICreator.button(op, rd, 'text', onClick)



