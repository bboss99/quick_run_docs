import bpy

def get_sub_md():
    # texts, onClicks, toolTipTexts,toolTipImages, get_submenu_data_fns, params
    primitives = ['plane','cube','circle','uv_sphere','ico_sphere','cylinder']
    create_primitive = lambda caller:exec(f"bpy.ops.mesh.primitive_{caller.param}_add()")
    count = len(primitives)
    return primitives, [create_primitive]*count, primitives, ['']*count, [None]*count, primitives