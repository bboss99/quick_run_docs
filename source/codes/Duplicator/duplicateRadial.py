from boss.ui_creator import UICreator,Boss_OT_base_ui,RectData
import bpy
from mathutils import Vector, Euler, Matrix
import math


copies = 0
deleted = 0
dict_objsToDelete:dict = {}
dict_createdObj:dict = {}
dict_collections:dict = {}

vff_pivotPos            : None
ff_angle                : None
tf_axis                 : None
cb_inNewCollection      : None
cb_collectionUnderScene : None
if_copies               : None

# There are two ways to make object disappear
# obj.hide_set(True), to hide object.
# deleted objects will be hidden.

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

def delete_collection(collection_name):
    allColls = bpy.data.collections
    allColls.remove(bpy.data.collections[collection_name], do_unlink=True)

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

def cleanup():
    print('cleanup')
    allObjs = bpy.data.objects

    for objList in dict_objsToDelete.values():
        for o in objList:
            allObjs.remove(o, do_unlink=True)

def onCopiesChanged(caller):
    global copies
    global deleted
    global dict_objsToDelete

    newCopies = caller.value

    if newCopies > copies:
        # new objects will be created.

        objToCreateCnt = newCopies - copies

        # check if objects are available in deleted
        if deleted >= objToCreateCnt:
            # enough objects are in deleted dict.
            # new objects won't be created.

            for (obj, deletedObjList),createdObjList in zip(dict_objsToDelete.items(),dict_createdObj.values()):
                moveToCreated = deletedObjList[:objToCreateCnt]
                del deletedObjList[:objToCreateCnt]
                for mtc in moveToCreated:
                    mtc.hide_set(False)
                    createdObjList.append(mtc)

            deleted = deleted - objToCreateCnt
        else:
            # not enough objects in deleted
            for obj, deletedObjList in dict_objsToDelete.items():
                moveToCreated = deletedObjList[:]
                deletedObjList.clear()
                for mtc in moveToCreated:
                    mtc.hide_set(False)

            toCreateMore = objToCreateCnt - deleted

            for (obj, coll), createdObjList in zip(dict_collections.items(), dict_createdObj.values()):
                for i in range(toCreateMore):
                    ob = copyObj(obj, False, False, True)
                    ob.name = obj.name + '_dupli_' + str(copies + i)
                    coll.objects.link(ob)
                    createdObjList.append(ob)

            deleted = 0
    else:
        # objects will be destroyed.
        # number of objects to delete from each object list
        objToDelCnt = copies - newCopies
        for obj, createdObjList in dict_createdObj.items():
            temp = createdObjList[-objToDelCnt:]

            del createdObjList[-objToDelCnt:]

            for t in reversed(temp):
                t.hide_set(True)
                dict_objsToDelete[obj].insert(0,t)


        deleted += objToDelCnt

    copies = newCopies
    # print('createdObj')
    # for ol in dict_createdObj.values():
    #     for o in ol:
    #         print(f'\t{o.name}')
    #
    # print('deletedObjList')
    # for ol in dict_objsToDelete.values():
    #     for o in ol:
    #         print(f'\t{o.name}')
    #
    # print(f'deleted:\t{deleted}')
    # print(f'copies :\t{copies}')
    placeObjects()

def getCollection(obj):
    inNewCollection, collectionUnderScene = (cb_inNewCollection.value, cb_collectionUnderScene.value)
    C = bpy.context
    objCollection = find_collection(C, obj)

    # new_collection is the collection where duplicated objects will be
    # childed.

    new_collection = objCollection

    if inNewCollection:
        if collectionUnderScene:
            new_collection = make_collection(obj.name + '_duplicated', C.scene.collection)
        else:
            new_collection = make_collection(obj.name + '_duplicated', objCollection)

    return new_collection

def placeObjects():
    pivotPos, axis, angle = (vff_pivotPos.value, tf_axis.value, ff_angle.value)
    global dict_createdObj
    global dict_collections

    for i, ((obj, coll), objList) in enumerate(zip(dict_createdObj.items(), dict_createdObj.values())):

        initMat = obj.matrix_world

        for i,ob in enumerate(objList):
            # transformations:
            mat = getRotatedMatrix(initMat, Vector(pivotPos), axis, angle * i)
            ob.matrix_world = mat

def onUnderSceneCollectionPressed():
    if not cb_inNewCollection.value:
        return
    else:
        if cb_collectionUnderScene.value:
            for obj, coll in dict_collections.items():
                objColl = find_collection(bpy.context, obj)
                objColl.children.unlink(coll)
                bpy.context.scene.collection.children.link(coll)
        else:
            for obj, coll in dict_collections.items():
                objColl = find_collection(bpy.context, obj)
                bpy.context.scene.collection.children.unlink(coll)
                objColl.children.link(coll)


def onNewCollectionChanged():
    global dict_collections
    global dict_createdObj

    for obj, objList in dict_createdObj.items():
        oldColl = dict_collections[obj]
        newColl = getCollection(obj)

        if newColl == oldColl:
            return
        else:
            dict_collections[obj] = newColl
            for o in objList:
                oldColl.objects.unlink(o)
                newColl.objects.link(o)
            if cb_inNewCollection.value:
                pass
            else:
                delete_collection(obj.name + '_duplicated')

def onAxisChanged():
    temp = tf_axis.value.upper()
    if len(temp) > 1:
        temp = temp[0]

    if temp not in ('X','Y','Z'):
        temp = 'X'

    tf_axis.setValue(temp)
    placeObjects()


def ui_elements_inCircle(op: Boss_OT_base_ui):
    """ duplicated selected objects in order in new collection """

    objs = bpy.context.selected_objects
    if len(objs) < 1:
        return {'no object selected, select something'}

    global vff_pivotPos
    global ff_angle
    global tf_axis
    global cb_inNewCollection
    global cb_collectionUnderScene
    global if_copies

    vff_pivotPos = UICreator.vectorFloatField(op, (0, 0, 100, 50), (0.0, 0.0, 0.0),placeObjects)

    ff_angle = UICreator.floatField(op, vff_pivotPos.rectData.getTop(5), 30.0, placeObjects)

    tf_axis = UICreator.textField(op, ff_angle.button.rectData.getTop(5), 'Z')

    cb_inNewCollection = UICreator.checkBox(op, tf_axis.button.rectData.getTop(5), 'new collection', False, onNewCollectionChanged)

    cb_collectionUnderScene = UICreator.checkBox(op, cb_inNewCollection.button.rectData.getTop(5), 'under the scene', False, onUnderSceneCollectionPressed)

    if_copies = UICreator.intField(op, cb_collectionUnderScene.button.getTop(5), 3, onCopiesChanged)

    global copies
    global dict_createdObj
    global dict_collections

    copies = if_copies.value

    # create collections in the beginning

    dict_collections = {obj : getCollection(obj) for obj in objs}

    dict_createdObj.update({o: [] for o in objs})
    dict_objsToDelete.update({o: [] for o in objs})

    # Create new objects and link those to collection
    for (obj, coll), createdObjList in zip(dict_collections.items(), dict_createdObj.values()):
        for i in range(copies):
            ob = copyObj(obj, False, False, True)
            ob.name = obj.name + '_dupli_' + str(i)
            coll.objects.link(ob)
            createdObjList.append(ob)

    # place objects
    placeObjects()

    op.onCancel.append(cleanup)

