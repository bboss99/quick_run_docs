import bpy

primitives = ['plane','cube','circle','uv_sphere','ico_sphere','cylinder']

def create_primitive(caller):  
    exec(f"bpy.ops.mesh.primitive_{caller.param}_add()")

def get_sub_md():
    # texts, onClicks, toolTipTexts,toolTipImages, get_submenu_data_fns, params
    
    count = len(primitives)
    return primitives, [create_primitive]*count, primitives, ['']*count, [None]*count, primitives