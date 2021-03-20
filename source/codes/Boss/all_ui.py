from boss.ui_creator import Button, TextField, RectData
from boss.ui_creator import UICreator as cc

def onClick(caller: Button):
    print(caller)

def onTextField_TextChanged(caller: TextField):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')

def onTextField_ValueChanged(caller: TextField):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')

def onTextField_EnterPressed(caller: TextField):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')

def onValueChange(caller):
    print(type(caller).__name__, caller.value)

def onTextChange(caller:TextField):
    print(type(caller).__name__, caller.value)

def onEnterPress(caller:TextField):
    print(type(caller).__name__, caller.value)



def ui_elements(op):
    cc.deleteAllUi(op)  # to delete all existing ui
    mouse_x, mouse_y = cc.mouse_xy(op)
    btn_height, btn_width = 50, 200

    rd = RectData(mouse_x, mouse_y - 50, btn_width, btn_height)

    btn_title = cc.button(op, rd, text='Title Bar',
                                 ttt='This is a button, you can drag it'
                                 )

    space = 0#10

    rd = rd.getBottom(space)

    cc.button(
        op,rd,
        text='text',
        buttonData=onClick,
        parent = btn_title,
        canDrag = False,
        ttt='This is a button'
    )

    rd = rd.getBottom(space)
    cc.textField(
        op,rd,
        onTextChange=onTextField_TextChanged,
        onValueChange=onTextField_ValueChanged,
        onEnterPress=onTextField_EnterPressed,
        parent = btn_title,
        canDrag = False,
        ttt='This is a TextField'
    )

    rd = rd.getBottom(space)
    cc.intField(
        op,rd,
        value=1,
        onTextChange=onTextChange,
        onValueChange=onValueChange,
        onEnterPress=onEnterPress,
        parent = btn_title,
        canDrag = False,
        ttt='This is a IntField'

    )

    rd = rd.getBottom(space)
    cc.floatField(
        op,rd,
        value=0.0,
        onTextChange=onTextChange,
        onValueChange=onValueChange,
        onEnterPress=onEnterPress,
        parent = btn_title,
        canDrag = False,
        ttt='This is a FloatField'
    )

    rd = rd.getBottom(space)
    cc.checkBox(
        op,rd,
        text='text',
        value=True,
        onValueChange=onValueChange,
        parent = btn_title,
        canDrag = False,
        ttt='This is a Checkbox(boolean)'
    )
    rd = rd.getBottom(space)

    cc.vectorBooleanField(
        op,rd,
        value=(True, False, True),
        onValueChange=onValueChange,
        parent = btn_title,
        canDrag = False,
        ttt='This is VectorBooleanField'
    )

    rd = rd.getBottom(space)

    cc.vectorFloatField(
        op,rd,
        value=(0.0, 0.0, 0.0),
        onValueChange=onValueChange,
        onTextChange=onTextChange,
        onEnterPress=onEnterPress,
        parent = btn_title,
        canDrag = False,
        ttt='This is VectorFloatField'
    )

    rd = rd.getBottom(space)

    cc.vectorIntField(
        op, rd,
        value=(0, 0, 0),
        onValueChange=onValueChange,
        onTextChange=onTextChange,
        onEnterPress=onEnterPress,
        parent = btn_title,
        canDrag = False,
        ttt='This is VectorIntField'
    )

