from boss.ui_creator import *
from boss.ui_creator import UICreator

def onClick(caller: Button):
    print(caller)

def onTextField_TextChanged(caller):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')

def onTextField_ValueChanged(caller:TextField):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')

def onTextField_EnterPressed(caller:TextField):
    print(type(caller).__name__, f'value - {caller.value}, text - {caller.text}')


def onValueChange(caller):
    print(type(caller).__name__, caller.value)

def onTextChange(caller):
    print(type(caller).__name__, caller.value)

def onEnterPress(caller):
    print(type(caller).__name__, caller.value)


def ui_elements(op: Boss_OT_base_ui):
    UICreator.deleteAllUi(op)  # to delete all existing ui
    btn_width, btn_height = 150, 40
    space = 10
    rr = UICreator.rr(op)
    rd = RectData(
        op.uip.mouse_x,
        rr.height - 150,
        # op.uip.mouse_y - btn_height,
        btn_width,
        btn_height
    )

    UICreator.button(
        op=op,
        rectData=rd,
        text='btn_text',
        buttonData=None,
        ttt='button tooltip',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False,
        param=None
    )

    rd = rd.getBottom(space)
    UICreator.textField(
        op,
        rectData=rd,
        onTextChange=onTextField_TextChanged,
        onValueChange=onTextField_ValueChanged,
        onEnterPress=onTextField_EnterPressed,
        ttt='This is tool_tip_text (ttt)',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False
    )

    rd = rd.getBottom(space)
    UICreator.intField(
        op,
        rectData=rd,
        value=1,
        onTextChange=onTextChange,
        onValueChange=onValueChange,
        onEnterPress=onEnterPress,
        ttt='This is tool_tip_text (ttt)',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False

    )

    rd = rd.getBottom(space)
    UICreator.floatField(
        op,
        rectData=rd,
        value=0.0,
        onTextChange=onTextChange,
        onValueChange=onValueChange,
        onEnterPress=onEnterPress,
        ttt= 'This is tool_tip_text (ttt)',
        tti = r'C:\Users\abc\Desktop\boss_location.png',
        canDrag = True,
        parent = None,
        rectIsLocal = False
    )

    rd = rd.getBottom(space)
    UICreator.checkBox(
        op=op,
        rectData=rd,
        text='checkBox',
        value=False,
        onValueChange=None,
        ttt='checkBox',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False,
        param=None
    )
    rd = rd.getBottom(space)

    UICreator.vectorBooleanField(
        op,
        rectData=rd,
        value=(True, False, True),
        onValueChange=onValueChange,
        ttt='This is tool_tip_text (ttt)',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False

    )

    rd = rd.getBottom(space)

    UICreator.vectorFloatField(
        op,
        rectData=rd,
        value=(0.0, 0.0, 0.0),
        onValueChange=onValueChange,
        onTextChange=onTextChange,
        onEnterPress=onEnterPress,
        ttt='This is tool_tip_text (ttt)',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False
    )

    rd = rd.getBottom(space)

    UICreator.vectorIntField(
        op,
        rectData=rd,
        value=(0, 0, 0),
        onValueChange=onValueChange,
        onTextChange=onTextChange,
        onEnterPress=onEnterPress,
        ttt='This is tool_tip_text (ttt)',
        tti=r'C:\Users\abc\Desktop\boss_location.png',
        canDrag=True,
        parent=None,
        rectIsLocal=False
    )
