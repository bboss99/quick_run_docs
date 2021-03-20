from boss.ui_creator import *


btns = {}
element_width = 200
element_height = 25

def getJsonPath():
    from os.path import dirname, join
    return join(dirname(__file__), f'_{__name__}.json')

json_path = getJsonPath()

def onClicked(caller):
    op:Boss_OT_base_ui = caller.op
    global btns

    name = f'btn_{len(btns)+1}'
    b = QButton.button(op,RectData.centeredAt(op.uip.mouse_x,op.uip.mouse_y,element_width,element_height),name)

    btns[name] = b


def printBtns():
    from boss.utils import json_dump
    json_dump(json_path, {k:v.rectData.getTuple() for k,v in btns.items()})

def ui_elements(op:Boss_OT_base_ui):
    op.uip.deleteAllUi()
    QButton(op, op.uip.region_rect.copy(), PanelData(panelType='none'), buttonData=ButtonData(onClicked))

    global btns
    from boss.utils import json_loadPath

    dict_locs = json_loadPath(json_path)

    for k,v in dict_locs.items():
        btns[k] = QButton.button(op,RectData(*v),k)

    op.uip.escapeFn.append(printBtns)
