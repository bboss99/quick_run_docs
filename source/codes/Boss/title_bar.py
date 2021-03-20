from boss.ui_creator import RectData
from boss.ui_creator import UICreator as cc

def onClick(caller):
    print(caller)

def ui_elements(op):
    cc.deleteAllUi(op)  # to delete all existing ui
    mouse_x, mouse_y = cc.mouse_xy(op)
    btn_height, btn_width = 50, 200

    rd = RectData(mouse_x, mouse_y - 50, btn_width, btn_height)

    btn_title = cc.button(op, rd, text='Title Bar')

    space = 10

    rd = rd.getBottom(space)

    cc.button(
        op,rd,
        text='button 1',
        buttonData=onClick,
        parent = btn_title,
        canDrag = False,
    )

    rd = rd.getBottom(space)

    cc.button(
        op, rd,
        text='button 2',
        buttonData=onClick,
        parent=btn_title,
        canDrag=False,
    )

