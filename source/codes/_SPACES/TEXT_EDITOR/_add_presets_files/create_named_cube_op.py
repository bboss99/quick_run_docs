import bpy

class OBJECT_OT_create_named_cube(bpy.types.Operator):
    bl_idname = 'object.create_named_cube'
    bl_label = 'Create Named Cube'
    cubeName : bpy.props.StringProperty(name='cubeName',default='Cube')

    def invoke(self, context, event):        
        return context.window_manager.invoke_props_dialog(self, width=250)

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add(size=2)
        context.object.name = self.cubeName
        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout
        layout.prop(self,'cubeName')

def register():
    bpy.utils.register_class(OBJECT_OT_create_named_cube)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_named_cube)


if __name__ == "__main__":
    register()
