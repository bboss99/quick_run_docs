# purge, it will removed unused deleted data.
import bpy

def purge():
    # purge won't run more than 5 times.
    # for any unknown reason, lets say their is some cyclic dependency and purge never return
    # {'CANCELLED'}, which it returns when it has nothing to purge
    # when I am using api, I don't fully understand, I use this trick to avoid infinite loop
    safety_cnt = 5
    for i in range(safety_cnt):
        op_result = bpy.ops.outliner.orphans_purge()
        # returns {'FINISHED'} or {'CANCELLED'}
        if op_result == {'CANCELLED'}:
            if i == 0:
                print(f'ran purge {i + 1} times, there was nothing to purge')
            else:
                print(f'ran purge {i + 1} times')
            return
    print(f"purging {safety_cnt} times wasn't enough, run once more")

purge()