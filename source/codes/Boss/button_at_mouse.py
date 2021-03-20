from boss.ui_creator import UICreator

def onClick(caller):
    print('button is clicked')
    caller.op.quit()  # to quit after the button is clicked.

def ui_elements(op):
    UICreator.deleteAllUi(op)  # to delete all existing ui

    btn_width, btn_height = 100, 40

    mouse_x, mouse_y = UICreator.mouse_xy(op)

    rd = (mouse_x, mouse_y - btn_height, btn_width, btn_height)

    UICreator.button(op, rd, 'btn_text', onClick)
