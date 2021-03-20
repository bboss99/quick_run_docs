import bpy
from mathutils import Vector
import math
#scale curve to 

def getCamera():
    cam = bpy.context.scene.camera
    if not cam:
        area = bpy.context.area.type
        bpy.context.area.type = 'VIEW_3D'
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW',
                                  location=(0, 0, 0), rotation=(0.0, 0.0, math.radians(180.0)))
        bpy.ops.view3d.object_as_camera()
        bpy.context.area.type = area
        return bpy.context.scene.camera
    else:
        return cam


# create curve

bpy.ops.curve.primitive_bezier_circle_add(radius=10, enter_editmode=False, location=(0, 0, 0))
targetCurve = bpy.context.object
targetCurve.name = '_camPathCurve'
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
camTarget = bpy.context.object
camTarget.name = '_camTarget'
print(targetCurve)
print(camTarget)

targetCurve.select_set(False)
camTarget.select_set(False)

cam = getCamera()
cam.location = Vector((0,0,0))

print(cam)


bpy.ops.object.select_all(action='DESELECT')
cam.select_set(True)
bpy.context.view_layer.objects.active = cam


bpy.ops.object.constraint_add(type='FOLLOW_PATH')
bpy.context.object.constraints["Follow Path"].target = targetCurve
bpy.context.object.constraints["Follow Path"].forward_axis = 'TRACK_NEGATIVE_X'
bpy.context.object.constraints["Follow Path"].up_axis = 'UP_Z'
bpy.context.object.constraints["Follow Path"].use_curve_follow = True


bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = None

cam.select_set(True)
bpy.context.view_layer.objects.active = cam



bpy.ops.object.constraint_add(type='DAMPED_TRACK')

bpy.context.object.constraints["Damped Track"].track_axis = 'TRACK_NEGATIVE_Z'


bpy.context.object.constraints["Damped Track"].target = camTarget


#addingKeyframe
duration = 150
bpy.context.object.constraints["Follow Path"].offset = 0 #0 to 100
bpy.context.object.constraints["Follow Path"].keyframe_insert(data_path="offset", frame=1)

#bpy.context.scene.frame_current = duration
bpy.context.object.constraints["Follow Path"].offset = 100
bpy.context.object.constraints["Follow Path"].keyframe_insert(data_path="offset", frame=duration)

