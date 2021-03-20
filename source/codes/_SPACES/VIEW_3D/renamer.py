import bpy
from boss.ui_creator import *

# for ui
start_point = [-1, -1]
element_height = 25
element_width = 200
element_space = 5
screen_margin = [50, 100]

#
sels: list = []

class RTextField(TextField):
    def _makeEditable(self, *args):
        super(RTextField, self)._makeEditable()

        o = self.param

        # deselect all
        bpy.ops.object.select_all(action='DESELECT')
        # select
        o.select_set(True)
        # make active
        bpy.context.view_layer.objects.active = o

def renameObj(caller: TextField):
    # print(caller.param, caller.value)
    caller.param.name = caller.value


def ui_elements(op: Boss_OT_base_ui):
    op.uip.deleteAllUi()

    global sels
    sels = bpy.context.selected_objects

    uip = op.uip

    initX = op.uip.mouse_x if start_point[0] == -1 else start_point[0]
    initY = op.uip.mouse_y if start_point[1] == -1 else start_point[1]

    rd = RectData(
        initX,
        initY - element_height,
        element_width,
        element_height
    )

    reg_height = uip.region_rect.height - screen_margin[1]

    for o in sels:
        rd = rd.getTop(5)
        if rd.yMax > reg_height:
            initX += (element_width + element_space)
            rd.setPosition(initX, screen_margin[0])

        RTextField(op, rd, value=o.name, param=o, onValueChange=renameObj)

    bpy.ops.object.select_all(action='DESELECT')
