import bpy
from boss.ui_creator import TextField, UICreator, Boss_OT_base_ui, RectData

# for ui
element_height = 25
element_width = 200
element_space = 5
screen_margin = [50, 100]

# for selected object
sels: list = []

def renameObj(caller: TextField):
    caller.param.name = caller.value

def ui_elements(op: Boss_OT_base_ui):
    UICreator.deleteAllUi(op)

    global sels
    sels = bpy.context.selected_objects

    mouse_x,mouse_y = UICreator.mouse_xy(op)

    initX = mouse_x
    initY = mouse_y

    rd = RectData(
        initX,
        initY - element_height,
        element_width,
        element_height
    )

    reg_height = UICreator.rr(op).height - screen_margin[1]

    for o in sels:
        rd = rd.getTop(5)
        if rd.yMax > reg_height:
            initX += (element_width + element_space)
            rd.setPosition(initX, screen_margin[0])

        UICreator.textField(op, rd, text=o.name, param=o, onValueChange=renameObj)

    bpy.ops.object.select_all(action='DESELECT')
