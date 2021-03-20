import bpy
from boss.ui_creator import *


def onClick(caller: Button):
    print(caller)

def onTextField_TextChanged(caller:TextField):
    print(caller, f'value - {caller.value}, text - {caller.text}')

def onTextField_ValueChanged(caller:TextField):
    print(caller, f'value - {caller.value}, text - {caller.text}')

def onTextField_EnterPressed(caller:TextField):
    print(caller, f'value - {caller.value}, text - {caller.text}')


def onValueChange(caller):
    print(caller, caller.value)

def onTextChange(caller:Button):
    print(caller, caller.value)

def onEnterPress(caller:Button):
    print(caller, caller.value)


def ui_elements(op: Boss_OT_base_ui):
    op.uip.deleteAllUi()  # to delete all existing ui
    btn_width, btn_height = 150, 40
    space = 10
    rd = RectData(
        op.uip.mouse_x,
        op.uip.mouse_y - btn_height,
        btn_width,
        btn_height
    )

    UICreator.button(op, rd, 'btn_text', onClick)
    rd = rd.getBottom(space)
    UICreator.button(
        op,
        rectData=rd,
        text='text',
        buttonData=onClick,
    )

    rd = rd.getBottom(space)
    UICreator.textField(
        op,
        rectData=rd,
        onTextChange=onTextField_TextChanged,
        onValueChange=onTextField_ValueChanged,
        onEnterPress=onTextField_EnterPressed
    )

    rd = rd.getBottom(space)
    UICreator.intField(
        op,
        rectData=rd,
        value=1,
        onTextChange=onTextChange,
        onValueChange=onValueChange,
        onEnterPress=onEnterPress
    )

    rd = rd.getBottom(space)
    UICreator.floatField(
        op,
        rectData=rd,
        value=0.0,
        onTextChange=onTextChange,
        onValueChange=onValueChange,
        onEnterPress=onEnterPress
    )

    rd = rd.getBottom(space)
    UICreator.checkBox(
        op,
        rectData=rd,
        text='text',
        value=True,
        onValueChange=onValueChange
    )
    rd = rd.getBottom(space)

    UICreator.vectorBooleanField(
        op,
        rectData=rd,
        value=(True, False, True),
        onValueChange=onValueChange
    )

    rd = rd.getBottom(space)

    UICreator.vectorFloatField(
        op,
        rectData=rd,
        value=(0.0, 0.0, 0.0),
        onValueChange=onValueChange,
        onTextChange=onTextChange,
        onEnterPress=onEnterPress
    )

    rd = rd.getBottom(space)

    UICreator.vectorIntField(
        op,
        rectData=rd,
        value=(0, 0, 0),
        onValueChange=onValueChange,
        onTextChange=onTextChange,
        onEnterPress=onEnterPress
    )
