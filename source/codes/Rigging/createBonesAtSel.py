import bpy

'''
Notes:
    To change mode:
        #bpy.ops.object.mode_set(mode='EDIT')
        #bpy.ops.object.mode_set(mode='OBJECT')

    #select the bone.
    bpy.data.objects["Cube_armature"].data.bones["Cube"].select = True
'''

createdArmature = ''


def setParent(objToParent,arma,parent_bone_name):
    bpy.ops.object.select_all(action='DESELECT')
    arma.select_set(True)
    bpy.context.view_layer.objects.active = arma 

    bpy.ops.object.mode_set(mode='EDIT')

    arma.data.edit_bones.active = arma.data.edit_bones[parent_bone_name]

    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')
    objToParent.select_set(True)
    arma.select_set(True)
    bpy.context.view_layer.objects.active = arma

    # the active object will be the parent of all selected object

    bpy.ops.object.parent_set(type='BONE', keep_transform=True)


def createEmptyArmature(armName):

    # create an armature and enter edit mode.
    bpy.ops.object.armature_add(enter_editmode=True, location=(0,0,0))

    # select all bones (one bone which was created by default)
    bpy.ops.armature.select_all(action='SELECT')

    # delete the default bone.
    bpy.ops.armature.delete()

    global createdArmature
    createdArmature = bpy.context.object

    # set name.
    bpy.context.object.name=armName
    # name child armature node.
    bpy.context.object.data.name = armName+'_'


for runOnce in range(1):
    selObjs = bpy.context.selected_objects

    if(len(selObjs) <1 ):
        print('no object selected.')
        break
    #deselect all objects in objects mode.
    bpy.ops.object.select_all(action='DESELECT')

    createEmptyArmature(selObjs[0].name+'_armature')

    print(createdArmature)

    for obj in selObjs:
        bpy.context.scene.cursor.location=obj.location
        objName = obj.name
        bpy.ops.armature.bone_primitive_add(name=objName+'_bone')

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    boneNames = []

    for i in createdArmature.data.bones:
        boneNames.append(i.name)

    for i in range(len(boneNames)):
        setParent(selObjs[i],createdArmature,boneNames[i])

