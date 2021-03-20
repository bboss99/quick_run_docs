import bpy
for i in bpy.data.materials:
    if "Diffuse BSDF" in i.node_tree.nodes:
        i.diffuse_color = i.node_tree.nodes["Diffuse BSDF"].inputs[0].default_value
    elif "Principled BSDF" in i.node_tree.nodes:
        i.diffuse_color = i.node_tree.nodes["Principled BSDF"].inputs[0].default_value