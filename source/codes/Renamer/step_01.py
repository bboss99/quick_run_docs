import bpy
from boss.ui_creator import TextField, UICreator, Boss_OT_base_ui


def renameObj(caller: TextField):
    caller.param.name = caller.value


def ui_elements(op: Boss_OT_base_ui):
    UICreator.deleteAllUi(op)  #  delete any existing UI

    o = bpy.context.object

    mouse_x, mouse_y = UICreator.mouse_xy(op)

    rd = (mouse_x, mouse_y - 25, 200, 25)

    UICreator.textField(op, rd, text=o.name, param=o, onValueChange=renameObj)
