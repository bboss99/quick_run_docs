import bpy

# create a curve circle, it will be camera's path.
bpy.ops.curve.primitive_bezier_circle_add(
    radius=10, enter_editmode=False, location=(0, 0, 0))

# declare a variable for selected object(curve), rename it and then deselect it.
camPathCurve = bpy.context.object
camPathCurve.name = '_camPathCurve'
camPathCurve.select_set(False)

# create an empty, it will be camera's target.
bpy.ops.object.empty_add(
    type='PLAIN_AXES', location=(0, 0, 0))

# declare a variable for selected object(empty), rename it and then deselect it.
camTarget = bpy.context.object
camTarget.name = '_camTarget'
camTarget.select_set(False)

# declare variable for camera and reset it's location and rotation
cam = bpy.context.scene.camera
cam.location = (0, 0, 0)
cam.rotation_euler = (0, 0, 0)


# select and make the camera active object
cam.select_set(True)
bpy.context.view_layer.objects.active = cam

# add 'follow_path' constraint and set target to the circle curve.
# and change other properties
bpy.ops.object.constraint_add(type='FOLLOW_PATH')
cam.constraints["Follow Path"].target = camPathCurve
cam.constraints["Follow Path"].forward_axis = 'TRACK_NEGATIVE_X'
cam.constraints["Follow Path"].up_axis = 'UP_Z'
cam.constraints["Follow Path"].use_curve_follow = True

# clear selection and clear active object
bpy.ops.object.select_all(action='DESELECT')
bpy.context.view_layer.objects.active = None

# select and make the camera active object
cam.select_set(True)
bpy.context.view_layer.objects.active = cam

# add 'damped_track' constraint and set target to Empty object
# which is camera's target and change other properties too
bpy.ops.object.constraint_add(type='DAMPED_TRACK')
cam.constraints["Damped Track"].track_axis = 'TRACK_NEGATIVE_Z'
cam.constraints["Damped Track"].target = camTarget

# adding keyframes for animating camera
frame_start = 1
frame_end = 150
cam.constraints["Follow Path"].offset = 0
cam.constraints["Follow Path"].keyframe_insert(data_path="offset", frame=frame_start)

# bpy.context.scene.frame_current = duration  # changing frame is not required
cam.constraints["Follow Path"].offset = 100
cam.constraints["Follow Path"].keyframe_insert(data_path="offset", frame=frame_end)
