import bpy

if 'qr_text' in bpy.data.texts:
    # exec(curText.as_string())
    exec(bpy.data.texts['qr_text'].as_string())
else:
    t = bpy.data.texts.new('qr_text')
    t.write('# paste code here\n')