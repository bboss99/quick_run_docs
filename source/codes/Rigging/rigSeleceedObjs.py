import bpy

createdArmature = ''

# region Collection Stuff, these are so common, I keep it in some separate module, like in modules folder.

def getSceneCollection():
    return bpy.context.scene.collection

def make_collection(name, parent_collection=None):
    if parent_collection == None:
        parent_collection = getSceneCollection()
    if name in bpy.data.collections:  # Does the collection already exist?
        # check parent collection
        return bpy.data.collections[name]
    else:
        new_collection = bpy.data.collections.new(name)
        parent_collection.children.link(new_collection)  # Add the new collection under a parent
        return new_collection

def findObjectCollection(context, item):
    collections = item.users_collection
    colLen = len(collections)

    if colLen > 0:
        for i in range(colLen):
            if not 'RigidBody' in collections[i].name:
                return collections[i]

    return context.scene.collection

def moveTo_collection(context, item, newColl):
    currentCollection = findObjectCollection(context, item)
    if currentCollection == newColl:
        return
    else:
        currentCollection.objects.unlink(item)
        newColl.objects.link(item)
#endregion

def setParent(objToParent, arma, parent_bone_name):
    bpy.ops.object.select_all(action='DESELECT')
    arma.select_set(True)
    bpy.context.view_layer.objects.active = arma

    bpy.ops.object.mode_set(mode='EDIT')

    arma.data.edit_bones.active = arma.data.edit_bones[parent_bone_name]

    bpy.ops.object.mode_set(mode='OBJECT')

    bpy.ops.object.select_all(action='DESELECT')  # deselect all objects
    objToParent.select_set(True)
    arma.select_set(True)
    bpy.context.view_layer.objects.active = arma
    # the active object will be the parent of all selected object

    bpy.ops.object.parent_set(type='BONE', keep_transform=True)


def createEmptyArmature(armName):
    # create a an armature and enter edit mode.
    bpy.ops.object.armature_add(enter_editmode=True, location=(0, 0, 0))

    # select all bones (one bone which was created by default)
    bpy.ops.armature.select_all(action='SELECT')

    # delete the default bone.
    bpy.ops.armature.delete()

    global createdArmature
    createdArmature = bpy.context.object
    # set name.
    bpy.context.object.name = armName
    # name child armature node.
    bpy.context.object.data.name = armName + '_'


for runOnce in range(1):
    selObjs = bpy.context.selected_objects

    if (len(selObjs) < 1):
        print('no object selected.')
        break
    # deselect all objects in objects mode.
    bpy.ops.object.select_all(action='DESELECT')

    createEmptyArmature(selObjs[0].name + '_armature')

    print(createdArmature)

    for obj in selObjs:
        bpy.context.scene.cursor.location = obj.location
        objName = obj.name
        bpy.ops.armature.bone_primitive_add(name=objName + '_bone')

    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.select_all(action='DESELECT')

    boneNames = []

    for i in createdArmature.data.bones:
        boneNames.append(i.name)

    for i in range(len(boneNames)):
        setParent(selObjs[i], createdArmature, boneNames[i])


cc_Col = make_collection(selObjs[0].name + 'cc_Col', getSceneCollection())

curves = []
for obj in selObjs:
    # bpy.context.scene.cursor.location=obj.location
    objName = obj.name
    bpy.ops.curve.primitive_bezier_circle_add(enter_editmode=False, location=obj.location.copy())
    cur = bpy.context.object
    cur.name = 'cc_' + objName
    cur.show_in_front = True
    moveTo_collection(bpy.context, cur, cc_Col)
    curves.append(cur)

i = 0
for b in createdArmature.pose.bones:
    crc = b.constraints.new('COPY_TRANSFORMS')
    crc.target = curves[i]
    i = i + 1
