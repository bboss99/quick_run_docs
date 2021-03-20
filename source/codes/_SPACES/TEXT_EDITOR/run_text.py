import bpy

curText = bpy.context.space_data.text
if curText:
    exec(curText.as_string())
else:
    t = bpy.data.texts.new('Text')
    t.write('# paste code here\n')
    bpy.context.space_data.text = t
