import bpy

# create cube
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD',
                                location=(0, 0, 0), scale=(1, 1, 1))

# create array
bpy.ops.object.modifier_add(type='ARRAY')

# create count = 5
bpy.context.object.modifiers["Array"].count = 5

# create step = 2
bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 2

# apply modifier
bpy.ops.object.modifier_apply(modifier="Array")

# enter editmode
bpy.ops.object.editmode_toggle()

bpy.ops.mesh.separate(type='LOOSE')

# exit editmode
bpy.ops.object.editmode_toggle()

# set pivot
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')