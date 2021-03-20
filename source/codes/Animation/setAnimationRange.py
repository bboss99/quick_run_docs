import bpy
import math

# get keyframes of object list
def get_keyframes(obj_list):
    keyframes = []
    for obj in obj_list:
        anim = obj.animation_data
        if anim is not None and anim.action is not None:
            for fcu in anim.action.fcurves:
                for keyframe in fcu.keyframe_points:
                    x, y = keyframe.co
                    if x not in keyframes:
                        keyframes.append((math.ceil(x)))
    return keyframes

# get all selected objects
selection = bpy.context.selected_objects

# check if selection is not empty
if selection:

    # get all frames with assigned keyframes
    keys = get_keyframes(selection)

    # print all keyframes
    print (keys)   

    # print first and last keyframe
    print ("{} {}".format("first keyframe:", keys[0]))
    print ("{} {}".format("last keyframe:", keys[-1]))

    bpy.context.scene.frame_start = keys[0]
    bpy.context.scene.frame_end = keys[-1]
else:
    print ('nothing selected')