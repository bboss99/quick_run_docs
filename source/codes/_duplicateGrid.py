# "name": "Duplicates selected objects in Grid"
# bl_label = "My AN Duplicate Objects in Circle"

from boss.ui_creator import UICreator,Boss_OT_base_ui,RectData
import bpy
from mathutils import Vector, Euler, Matrix
import math


# axis = 'X','Y','Z'
def getRotatedMatrix(sourceMat, pivotPos, axis, angle):
    # sourceMat = source.matrix_world
    loc, rot, sca = sourceMat.decompose()

    pivOffset = loc - pivotPos

    locMat = Matrix.Translation(pivOffset)
    rotMat = rot.to_matrix().to_4x4()
    scaMat = Matrix.Diagonal(sca).to_4x4()

    pivMat = Matrix.Translation(pivotPos)

    mat_rotBy = Matrix.Rotation(math.radians(angle), 4, axis)

    mat_out = pivMat @ mat_rotBy @ locMat @ rotMat @ scaMat

    return mat_out


def find_collection(context, item):
    collections = item.users_collection
    if len(collections) > 0:
        return collections[0]
    return context.scene.collection


def make_collection(collection_name, parent_collection):
    if collection_name in bpy.data.collections:  # Does the collection already exist?
        return bpy.data.collections[collection_name]
    else:
        new_collection = bpy.data.collections.new(collection_name)
        parent_collection.children.link(new_collection)  # Add the new collection under a parent
        return new_collection


def copyObj(objToCopy, copyMesh, copyMat, copyAnim):
    ob = objToCopy.copy()
    if copyMesh:
        ob.data = ob.data.copy()
    if copyMat:
        for slot in ob.material_slots:
            slot.material = slot.material.copy()
    if copyAnim:
        if objToCopy.animation_data and objToCopy.animation_data.action:
            ob.animation_data.action = objToCopy.animation_data.action.copy()
        else:
            # print('object has no animation data')
            pass
    return ob

#
# class OBJECT_OT_my_an_duplicate_objects(bpy.types.Operator):
#     """duplicated selected objects in order in new collection"""
#     bl_label = "My AN Duplicate Objects"
#     bl_idname = "object.my_an_duplicate_objects"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     translate: bpy.props.FloatVectorProperty(name='translate', description='Translations', default=(0.0, 0.0, 0.0))
#     rotate: bpy.props.FloatVectorProperty(name='rotation', description='Translations', default=(0.0, 0.0, 0.0))
#     scale: bpy.props.FloatVectorProperty(name='scale', description='Scale', default=(0.0, 0.0, 0.0))
#
#     inNewCollection: bpy.props.BoolProperty(name='inNewCollection', description='copies object in new collection',
#                                             default=True)
#     collectionUnderScene: bpy.props.BoolProperty(name='collectionUnderScene',
#                                                  description='new collection should be under the scene', default=True)
#
#     times: bpy.props.IntProperty(name='times', description='duplicate that many times', default=1)
#     idOffset: bpy.props.IntProperty(name='idOffset', description='offset an id by this', default=0)
#
#     def execute(self, context):
#         C = context
#         objs = C.selected_objects
#
#         if len(objs) < 1:
#             return {'FINISHED'}
#
#         for t in range(len(objs)):
#             objCollection = find_collection(C, objs[t])
#
#             initLoc = objs[t].location
#             initRotInRadian = Vector(
#                 (math.radians(self.rotate[0]), math.radians(self.rotate[1]), math.radians(self.rotate[2])))
#             initSca = objs[t].scale
#
#             # new_collection is the collection where duplicated objects will be childed.
#             new_collection = objCollection
#             if self.inNewCollection:
#                 if self.collectionUnderScene:
#                     new_collection = make_collection(objs[t].name + '_duplicated', C.scene.collection)
#                 else:
#                     new_collection = make_collection(objs[t].name + '_duplicated', objCollection)
#
#             for i in range(self.times):
#                 ob = copyObj(objs[t], False, False, True)
#                 ob.name = objs[t].name + '_dupli_' + str(i)
#                 new_collection.objects.link(ob)
#
#                 offsetANProperties(objs[t], ob, i * self.idOffset)
#
#                 # transformations:
#                 ob.location = initLoc + Vector(self.translate) * i
#
#                 # convert initRot in degrees.
#                 # initRot = Vector( ( math.degrees(initRot[0]),math.degrees(initRot[1]),math.degrees(initRot[2]) ) )
#
#                 # offset in radian
#                 rotateInRadian = Vector(
#                     (math.radians(self.rotate[0]), math.radians(self.rotate[1]), math.radians(self.rotate[2])))
#                 v = initRotInRadian + rotateInRadian * i
#                 ob.rotation_euler = Euler(v, 'XYZ')
#
#                 ob.scale = initSca + Vector(self.scale) * i
#
#         return {'FINISHED'}
#
#
# class OBJECT_OT_my_an_duplicate_in_grid(bpy.types.Operator):
#     """duplicated selected objects in order in new collection"""
#     bl_label = "My AN Duplicate In Grid"
#     bl_idname = "object.my_an_duplicate_in_grid"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     distribution: bpy.props.EnumProperty(
#         name="distribution",
#         description="how to duplicate",
#         items=[
#             ("STEP", "step", "distribute by translate as step"),
#             ("RANGE", "range", "distribute by translate as Range"),
#         ],
#         default='STEP')
#
#     translate: bpy.props.FloatVectorProperty(name='translate', description='Translations', default=(3.0, 3.0, 3.0),
#                                              min=0.0)
#     times: bpy.props.IntVectorProperty(name='times', description='times', default=(3, 3, 3), min=1)
#
#     center: bpy.props.BoolVectorProperty(name='center', description='center', default=(True, True, True))
#     # rotate : bpy.props.FloatVectorProperty(name='rotation',description='Translations',default=(0.0,0.0,0.0))
#     # scale : bpy.props.FloatVectorProperty(name='scale',description='Scale',default=(0.0,0.0,0.0))
#
#     inNewCollection: bpy.props.BoolProperty(name='inNewCollection', description='copies object in new collection',
#                                             default=True)
#     collectionUnderScene: bpy.props.BoolProperty(name='collectionUnderScene',
#                                                  description='new collection should be under the scene', default=True)
#
#     # idOffset : bpy.props.IntProperty(name='idOffset',description='offset an id by this',default=0)
#
#     # def draw(self, context):
#     #     layout = self.layout
#     #     layout.prop(self,'distribution')
#     #     layout.prop(self,'translate')
#     #     layout.prop(self,'times')
#
#     def execute(self, context):
#         C = context
#         objs = C.selected_objects
#
#         if len(objs) < 1:
#             return {'FINISHED'}
#
#         for t in range(len(objs)):
#             objCollection = find_collection(C, objs[t])
#
#             initLoc = Vector((0, 0, 0))
#             step = Vector((0, 0, 0))  # gap between objects
#
#             if self.distribution == 'STEP':
#                 step = self.translate
#
#                 initLoc[0] = objs[t].location[0] - ((self.times[0] - 1) * step[0]) / 2 if self.center[0] else \
#                 objs[t].location[0]
#                 initLoc[1] = objs[t].location[1] - ((self.times[1] - 1) * step[1]) / 2 if self.center[1] else \
#                 objs[t].location[1]
#                 initLoc[2] = objs[t].location[2] - ((self.times[2] - 1) * step[2]) / 2 if self.center[2] else \
#                 objs[t].location[2]
#
#             else:
#
#                 step[0] = 0 if self.times[0] == 1 else self.translate[0] / (self.times[0] - 1)
#                 step[1] = 0 if self.times[1] == 1 else self.translate[1] / (self.times[1] - 1)
#                 step[2] = 0 if self.times[2] == 1 else self.translate[2] / (self.times[2] - 1)
#
#                 initLoc[0] = objs[t].location[0] if self.times[0] == 1 else (
#                     objs[t].location[0] - self.translate[0] / 2 if self.center[0] else objs[t].location[0])
#                 initLoc[1] = objs[t].location[1] if self.times[1] == 1 else (
#                     objs[t].location[1] - self.translate[1] / 2 if self.center[1] else objs[t].location[1])
#                 initLoc[2] = objs[t].location[2] if self.times[2] == 1 else (
#                     objs[t].location[2] - self.translate[2] / 2 if self.center[2] else objs[t].location[2])
#                 # initLoc[2] = objs[t].location[2] if self.times[2] == 1 else objs[t].location[2] - self.translate[2]/2
#
#             # initRotInRadian = Vector ( (math.radians(self.rotate[0]),math.radians(self.rotate[1]),math.radians(self.rotate[2])) )
#             # initSca = objs[t].scale
#             # new_collection is the collection where duplicated objects will be childed.
#             new_collection = objCollection
#             if self.inNewCollection:
#                 if self.collectionUnderScene:
#                     new_collection = make_collection(objs[t].name + '_duplicated', C.scene.collection)
#                 else:
#                     new_collection = make_collection(objs[t].name + '_duplicated', objCollection)
#
#             # for x axis.
#             for x in range(self.times[0]):
#                 for y in range(self.times[1]):
#                     for z in range(self.times[2]):
#                         ob = copyObj(objs[t], False, False, True)
#
#                         ob.name = objs[t].name + '_dupli_' + str(x) + '_' + str(y) + '_' + str(z)
#                         new_collection.objects.link(ob)
#
#                         # offsetANProperties(objs[t],ob,i*self.idOffset)
#
#                         # transformations:
#                         ob.location[0] = initLoc[0] + step[0] * x
#                         ob.location[1] = initLoc[1] + step[1] * y
#                         ob.location[2] = initLoc[2] + step[2] * z
#
#                         # convert initRot in degrees.
#                         # initRot = Vector( ( math.degrees(initRot[0]),math.degrees(initRot[1]),math.degrees(initRot[2]) ) )
#
#                         # offset in radian
#                         # rotateInRadian = Vector((math.radians(self.rotate[0]),math.radians(self.rotate[1]),math.radians(self.rotate[2])))
#                         # v = initRotInRadian + rotateInRadian*i
#                         # ob.rotation_euler = Euler(v,'XYZ')
#
#                         # ob.scale = initSca + Vector(self.scale)*i
#
#         return {'FINISHED'}
#         pass

#
# class OBJECT_OT_my_an_duplicate_collection(bpy.types.Operator):
#     """duplicated selected objects in order in new collection"""
#     bl_label = "My AN Duplicate collection"
#     bl_idname = "object.my_an_duplicate_collection"
#     bl_options = {'REGISTER', 'UNDO'}
#
#     copyRotate: bpy.props.BoolProperty(name='copyRotate', description='copies rotate in empty', default=True)
#     copyScale: bpy.props.BoolProperty(name='copyScale', description='copies scale in empty', default=False)
#
#     how: bpy.props.EnumProperty(
#         name="how",
#         description="how to duplicate",
#         items=[
#             ("DUPLIOBJS", "dupliObjs", "copy animation too"),
#             ("CREATEEMPTY", "createEmpty", "create empty at sel postion"),
#             ("CREATEEMPTYMOVEANIM", "createEmptyMoveAnim", "create empty with animation in empty"),
#             ("CREATEEMPTYCOPYANIM", "createEmptyCopyAnim", "create empty with animation in both"),
#         ],
#         default='CREATEEMPTY')
#     times: bpy.props.IntProperty(name='times', description='copies that many times', default=1)
#     idOffset: bpy.props.IntProperty(name='idOffset', description='offset an id by this', default=0)
#
#     def execute(self, context):
#         C = context
#         objs = C.selected_objects
#
#         if len(objs) < 1:
#             return {'FINISHED'}
#
#         objCollection = find_collection(C, objs[0])
#
#         if self.how == 'DUPLIOBJS':
#             for t in range(self.times):
#                 new_collection = make_collection(objCollection.name + '_dupli_' + str(t), C.scene.collection)
#                 for i in range(len(objs)):
#                     ob = copyObj(objs[i], False, False, True)
#                     ob.name = objs[i].name + '_dupli_' + str(t)
#                     new_collection.objects.link(ob)
#                     offsetANProperties(objs[i], ob, self.idOffset * i)
#
#
#         elif self.how == 'CREATEEMPTY':
#             for t in range(self.times):
#                 new_collection = make_collection(objCollection.name + '_empty_' + str(t), C.scene.collection)
#                 for i in range(len(objs)):
#                     empty = bpy.data.objects.new(objs[i].name + '_empty_' + str(t), None)
#                     empty.empty_display_size = .25
#                     empty.empty_display_type = 'PLAIN_AXES'
#                     new_collection.objects.link(empty)
#                     empty.location = objs[i].location
#
#                     if self.copyRotate:
#                         empty.rotation_euler = objs[i].rotation_euler
#                     if self.copyScale:
#                         empty.scale = objs[i].scale
#
#                     addANPropertiesWithOffset(objs[i], empty, self.idOffset * i)
#
#         elif self.how == 'CREATEEMPTYMOVEANIM':
#             for t in range(self.times):
#                 new_collection = make_collection(objCollection.name + '_empty_anim_' + str(t), C.scene.collection)
#                 for i in range(len(objs)):
#                     empty = bpy.data.objects.new(objs[i].name + '_empty_anim_' + str(t), None)
#                     empty.empty_display_size = .25
#                     empty.empty_display_type = 'PLAIN_AXES'
#                     new_collection.objects.link(empty)
#
#                     empty.location = objs[i].location
#
#                     if self.copyRotate:
#                         empty.rotation_euler = objs[i].rotation_euler
#                     if self.copyScale:
#                         empty.scale = objs[i].scale
#
#                     addANPropertiesWithOffset(objs[i], empty, self.idOffset * i)
#
#                     if objs[i].animation_data and objs[i].animation_data.action:
#                         new_animation_data = empty.animation_data_create()
#                         new_animation_data.action = objs[i].animation_data.action
#                         objs[i].animation_data.action = None
#                     else:
#                         # print('object has no animation data')
#                         pass
#
#         elif self.how == 'CREATEEMPTYCOPYANIM':
#             for t in range(self.times):
#                 new_collection = make_collection(objCollection.name + '_empty_anim_' + str(t), C.scene.collection)
#                 for i in range(len(objs)):
#                     empty = bpy.data.objects.new(objs[i].name + '_empty_anim_' + str(t), None)
#                     empty.empty_display_size = .25
#                     empty.empty_display_type = 'PLAIN_AXES'
#                     new_collection.objects.link(empty)
#
#                     empty.location = objs[i].location
#
#                     if self.copyRotate:
#                         empty.rotation_euler = objs[i].rotation_euler
#                     if self.copyScale:
#                         empty.scale = objs[i].scale
#
#                     addANPropertiesWithOffset(objs[i], empty, self.idOffset * i)
#
#                     if objs[i].animation_data and objs[i].animation_data.action:
#                         new_animation_data = empty.animation_data_create()
#                         new_animation_data.action = objs[i].animation_data.action
#                     else:
#                         # print('object has no animation data')
#                         pass
#
#         return {'FINISHED'}


def resetPositions():
    for t in range(len(objs)):
        objCollection = find_collection(C, objs[t])
        # initLoc = objs[t].location
        # rotate = vff_rotation.value
        # initRotInRadian = Vector((math.radians(rotate[0]), math.radians(rotate[1]), math.radians(rotate[2])))
        # initSca = objs[t].scale
        initMat = objs[t].matrix_world

        # new_collection is the collection where duplicated objects will be childed.
        new_collection = objCollection
        if cb_inNewCollection.value:
            if cb_collectionUnderScene.value:
                new_collection = make_collection(objs[t].name + '_duplicated', C.scene.collection)
            else:
                new_collection = make_collection(objs[t].name + '_duplicated', objCollection)

        for i in range(if_copies.value):
            ob = copyObj(objs[t], False, False, True)
            ob.name = objs[t].name + '_dupli_' + str(i)
            new_collection.objects.link(ob)

            # transformations:
            mat = getRotatedMatrix(initMat, Vector(vff_rotation.value), tf_axis.value, ff_angle.value * i)
            ob.matrix_world = mat

def ui_elements_inCircle(op:Boss_OT_base_ui):
    """duplicated selected objects in order in new collection"""

    C = bpy.context
    objs = C.selected_objects

    if len(objs) < 1:
        return {'no object selected, select something'}

    vff_pivotPos = UICreator.vectorFloatField(op, (0, 0, 100, 50), (0.0, 0.0, 0.0), resetPositions)

    ff_angle = UICreator.floatField(op, vff_pivotPos.rectData.getTop(5), 0.0, resetPositions)
    tf_axis = UICreator.textField(op, ff_angle.button.rectData.getTop(5), 'z', resetPositions)

    vff_rotation = UICreator.vectorFloatField(op,tf_axis.button.rectData.getTop(5), (0.0, 0.0, 0.0), resetPositions)
    vff_scale = UICreator.vectorFloatField(op, vff_rotation.rectData.getTop(5), (0.0, 0.0, 0.0), resetPositions)

    cb_inNewCollection = UICreator.checkBox(op, vff_scale.rectData.getTop(5),'new collection',True)

    cb_collectionUnderScene =  UICreator.checkBox(op, cb_inNewCollection.button.rectData.getTop(5),'under the scene',True)

    if_copies = UICreator.intField(op, cb_collectionUnderScene.button.getTop(5),1)
