# purge script for outliner space.

import bpy

safety_cnt = 5 
display_mode = bpy.context.space_data.display_mode

bpy.context.space_data.display_mode = 'ORPHAN_DATA'

for i in range(safety_cnt):
    op_result = bpy.ops.outliner.orphans_purge()    
    # returns {'FINISHED'} or {'CANCELLED'}
    if op_result == {'CANCELLED'}:
        break

bpy.context.space_data.display_mode = display_mode