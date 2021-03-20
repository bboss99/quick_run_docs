import bpy

def assignMaterial(obj,mat):
    # Assign it to object
    if obj.data.materials:
        # assign to 1st material slot
        obj.data.materials[0] = mat
    else:
        # no slots
        obj.data.materials.append(mat)

i = 0
for m in bpy.data.materials:
    bpy.ops.mesh.primitive_monkey_add(size=2, enter_editmode=False, location=(i, 0, 0))
    bpy.context.object.name = m.name
    assignMaterial(bpy.context.object,m)
    i+=4
