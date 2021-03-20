import bpy
bpy.ops.object.mode_set(mode = 'OBJECT')
bpy.ops.curve.primitive_bezier_curve_add(radius=1, enter_editmode=False, location=(0, 0, 0))
bpy.ops.object.editmode_toggle()
bpy.ops.curve.select_all(action='SELECT')
bpy.ops.curve.delete(type='VERT')
bpy.ops.object.editmode_toggle()

