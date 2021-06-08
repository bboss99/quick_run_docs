import bpy
from boss.ui_creator import UICreator, Boss_OT_base_ui,RectData,FieldValue

def create_grid():
    # create cube
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD',
                                    location=(0, 0, 0), scale=(1, 1, 1))
    sel_obj = bpy.context.object

    # add array modifier
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.ops.object.modifier_add(type='ARRAY')

    # change count = 5
    bpy.context.object.modifiers["Array"].count = 3
    # it's named Array.001 by default
    bpy.context.object.modifiers["Array.001"].count = 3
    bpy.context.object.modifiers["Array.002"].count = 1

    # change step = 2
    bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 2

    bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
    bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 2

    bpy.context.object.modifiers["Array.002"].relative_offset_displace[0] = 0
    bpy.context.object.modifiers["Array.002"].relative_offset_displace[1] = 0
    bpy.context.object.modifiers["Array.002"].relative_offset_displace[2] = 2
    return sel_obj


def apply_mods(caller):
    sel_obj = caller.param

    bpy.context.view_layer.objects.active = sel_obj

    # apply modifier
    bpy.ops.object.modifier_apply(modifier="Array")
    bpy.ops.object.modifier_apply(modifier="Array.001")
    bpy.ops.object.modifier_apply(modifier="Array.002")

    # enter editmode
    bpy.ops.object.editmode_toggle()

    bpy.ops.mesh.separate(type='LOOSE')

    # exit editmode
    bpy.ops.object.editmode_toggle()

    # set pivot
    bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')

    caller.op.quit()


def onCountChanged(caller):

    sel_obj = caller.param
    x,y,z = caller.value

    sel_obj.modifiers["Array"].count = x
    sel_obj.modifiers["Array.001"].count = y
    sel_obj.modifiers["Array.002"].count = z


def ui_elements(op: Boss_OT_base_ui):
    UICreator.deleteAllUi(op)

    sel_obj = create_grid()

    fv = FieldValue(
        value=(3, 3, 1),
        min=(0, 0, 0),
        max=(10, 10, 10),
        changeBy=(1, 1, 1)
    )
    vif_cnt = UICreator.vectorIntField(op, RectData(100, UICreator.rr(op).height - 150, 200, 50),
                                       value=fv,onValueChange= onCountChanged, param=sel_obj)

    UICreator.button(op, vif_cnt.rectData.getBottom(5), text='Apply', buttonData=apply_mods, param=sel_obj)
