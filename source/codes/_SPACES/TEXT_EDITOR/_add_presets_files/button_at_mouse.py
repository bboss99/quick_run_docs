import bpy
from boss.ui_creator import *

def onClick(caller:Button):
    print('button is clicked')
    caller.op.quit()  # to quit after the button is clicked.


def ui_elements(op:Boss_OT_base_ui):
    op.uip.deleteAllUi()  # to delete all existing ui
    btn_width, btn_height = 100, 40

    rd = RectData(
        op.uip.mouse_x,
        op.uip.mouse_y - btn_height,
        btn_width,
        btn_height
    )

    UICreator.button(op, rd, 'btn_text', onClick)
