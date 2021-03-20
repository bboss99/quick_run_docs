from boss.ui_creator import UICreator, ButtonData,RectData

def ui_elements(op):
    def onClicked():
        print('Button is Clicked')

    def dragging(some_param):
        print(some_param)

    def onWheel(caller, addby):
        caller.param += addby
        print('param is now', caller.param)

    buttonData=ButtonData(
                onClick=onClicked,
                onMouseEnter=lambda :print('mouse entered'),
                onMouseExit=lambda :print('mouse exited'),
                onWheelUp=(onWheel, 1),
                onWheelDown=(onWheel, -1),
                onDragBegin=(dragging, 'dragging is started'),
                onDrag=(dragging, "it's being dragged"),
                onDragEnd=(dragging, 'dragging is ended')
            )
    button = UICreator.button(
            op=op,
            rectData=RectData(10, 110, 200, 100),
            text='ButtonText',
            buttonData=buttonData,
            ttt='tool tip text',
            param=100
        )
