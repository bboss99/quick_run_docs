import bpy

animated_objs = []

for material in bpy.data.materials:
    if material.animation_data:
        for obj in bpy.data.objects:
            for slot in obj.material_slots:
                if slot.material == material:
                    animated_objs.append(obj)

for obj in bpy.data.objects:
    if obj.animation_data:
        animated_objs.append(obj)

for obj in animated_objs:
    obj.select_set(True)