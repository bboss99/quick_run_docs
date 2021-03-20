import bpy

# create cube
bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD',
                                location=(0, 0, 0), scale=(1, 1, 1))

# add array modifier
bpy.ops.object.modifier_add(type='ARRAY')
bpy.ops.object.modifier_add(type='ARRAY')

# change count = 5
bpy.context.object.modifiers["Array"].count = 5
# it's named Array.001 by default
bpy.context.object.modifiers["Array.001"].count = 5

# change step = 2
bpy.context.object.modifiers["Array"].relative_offset_displace[0] = 2
bpy.context.object.modifiers["Array.001"].relative_offset_displace[0] = 0
bpy.context.object.modifiers["Array.001"].relative_offset_displace[1] = 2


# apply modifier
bpy.ops.object.modifier_apply(modifier="Array")
bpy.ops.object.modifier_apply(modifier="Array.001")

# enter editmode
bpy.ops.object.editmode_toggle()

bpy.ops.mesh.separate(type='LOOSE')

# exit editmode
bpy.ops.object.editmode_toggle()

# set pivot
bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME', center='MEDIAN')