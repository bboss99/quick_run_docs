from boss.ui_creator import *


def onClick(caller):
    print('button is clicked')

    # caller.op.quit()  # to quit after the button is clicked.
    caller.op.uip.bla = None


def ui_elements(op):
    UICreator.deleteAllUi(op)  # to delete all existing ui

    btn_width, btn_height = 100, 100

    mouse_x, mouse_y = UICreator.mouse_xy(op)

    # rds = RectData(mouse_x, mouse_y - btn_height, btn_width, btn_height).getRight(5, count=5)
    # for rd in rds:
    #     b = Button(op,rd,PanelData('ttttttttttttttttttttttttttttt',clipRect=rd),ButtonData(onClick=onClick))
    # rd = RectData(mouse_x, mouse_y - btn_height, btn_width, btn_height)
    # Button(op,rd,PanelData('ttttttttttttttttttttttttttttt',clipRect=rd,name='b1'),ButtonData(onClick=onClick))
    # rd = rd.getRight(5)
    # Button(op,rd,PanelData('ttttttttttttttttttttttttttttt',clipRect=rd,name='b2'),ButtonData(onClick=onClick))

    tf = TextField()

