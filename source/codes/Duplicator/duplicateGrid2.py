# "name": "Duplicates selected objects in Grid"
# bl_label = "My AN Duplicate Objects in Grid"

from boss.ui_creator import UICreator,Boss_OT_base_ui,RectData,FieldValue
import bpy
from mathutils import Vector, Euler, Matrix
import math


total_copies = 0
deleted = 0

dict_objsToDelete:dict = {}
dict_createdObj:dict = {}
dict_collections:dict = {}


vbf_center                   :None
cb_inNewCollection           :None
cb_collectionUnderScene      :None
vif_copies                   :None
cb_distribution              :None
vff_translate                :None


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

def cleanup():
    print('cleanup')
    allObjs = bpy.data.objects

    renameObjs()
    for objList in dict_objsToDelete.values():
        for o in objList:
            allObjs.remove(o, do_unlink=True)

def renameObjs():
    copies = vif_copies.value
    for obj, objList in dict_createdObj.items():
        i = 0
        for x in range(copies[0]):
            for y in range(copies[1]):
                for z in range(copies[2]):
                    objList[i].name = obj.name + '_dupli_' + str(x) + '_' + str(y) + '_' + str(z)
                    i += 1

def onCopiesChanged():
    global total_copies
    global deleted
    global dict_objsToDelete

    copies = vif_copies.value
    new_total_copies = copies[0] * copies[1] * copies[2]

    if new_total_copies > total_copies:
        # new objects will be created.
        objToCreateCnt = new_total_copies - total_copies

        # check if objects are available in deleted
        if deleted >= objToCreateCnt:
            # enough objects are in deleted dict.
            # new objects won't be created.
            for (obj, deletedObjList), createdObjList in zip(dict_objsToDelete.items(), dict_createdObj.values()):
                moveToCreated = deletedObjList[:objToCreateCnt]
                del deletedObjList[:objToCreateCnt]
                for mtc in moveToCreated:
                    mtc.hide_set(False)
                    createdObjList.append(mtc)

            deleted = deleted - objToCreateCnt
        else:
            # not enough objects in deleted
            # first move all deleted to the created.
            for (obj, deletedObjList), createdObjList in zip(dict_objsToDelete.items(), dict_createdObj.values()):
                moveToCreated = deletedObjList[:]
                deletedObjList.clear()
                for mtc in moveToCreated:
                    mtc.hide_set(False)
                    createdObjList.append(mtc)

            toCreateMore = objToCreateCnt - deleted

            for (obj, coll), createdObjList in zip(dict_collections.items(), dict_createdObj.values()):
                for i in range(toCreateMore):
                    ob = copyObj(obj, False, False, True)
                    ob.name = obj.name + '_dupli_' + str(total_copies + deleted + i)
                    coll.objects.link(ob)
                    createdObjList.append(ob)

            deleted = 0
    else:
        # objects will be destroyed.
        # number of objects to delete from each object list
        objToDelCnt = total_copies - new_total_copies
        for obj, createdObjList in dict_createdObj.items():
            temp = createdObjList[-objToDelCnt:]

            del createdObjList[-objToDelCnt:]

            for t in reversed(temp):
                t.hide_set(True)
                dict_objsToDelete[obj].insert(0,t)


        deleted += objToDelCnt

    total_copies = new_total_copies

    placeObjects()

def placeObjects():
    center, distribution, translate, copies = (vbf_center.value, cb_distribution.value, vff_translate.value, vif_copies.value)

    global dict_createdObj
    global dict_collections

    for obj, objList in dict_createdObj.items():
        initLoc = Vector((0, 0, 0))
        step = Vector((0, 0, 0))  # gap between objects

        if distribution:
            step = translate
            initLoc[0] = obj.location[0] - ((copies[0] - 1) * step[0]) / 2 if center[0] else obj.location[0]
            initLoc[1] = obj.location[1] - ((copies[1] - 1) * step[1]) / 2 if center[1] else obj.location[1]
            initLoc[2] = obj.location[2] - ((copies[2] - 1) * step[2]) / 2 if center[2] else obj.location[2]

        else:
            step[0] = 0 if copies[0] == 1 else translate[0] / (copies[0] - 1)
            step[1] = 0 if copies[1] == 1 else translate[1] / (copies[1] - 1)
            step[2] = 0 if copies[2] == 1 else translate[2] / (copies[2] - 1)

            initLoc[0] = obj.location[0] if copies[0] == 1 else (obj.location[0] - translate[0] / 2 if center[0] else obj.location[0])
            initLoc[1] = obj.location[1] if copies[1] == 1 else (obj.location[1] - translate[1] / 2 if center[1] else obj.location[1])
            initLoc[2] = obj.location[2] if copies[2] == 1 else (obj.location[2] - translate[2] / 2 if center[2] else obj.location[2])


        i = 0
        for x in range(copies[0]):
            for y in range(copies[1]):
                for z in range(copies[2]):
                    # transformations:
                    objList[i].location[0] = initLoc[0] + step[0] * x
                    objList[i].location[1] = initLoc[1] + step[1] * y
                    objList[i].location[2] = initLoc[2] + step[2] * z
                    i += 1

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

def ui_elements_inGrid(op: Boss_OT_base_ui):
    """ duplicated selected objects in order in new collection """
    ttt_under_scene = (
    'If collection is not on, then ignored',
    'otherwise created collection will be under',
    "'Scene collection' if on, and under object's",
    'collection if off '
    )

    objs = bpy.context.selected_objects

    if len(objs) < 1:
        return {'no object selected, select something'}

    global vbf_center
    global cb_inNewCollection
    global cb_collectionUnderScene
    global vif_copies
    global cb_distribution
    global vff_translate

    global total_copies
    global dict_createdObj
    global dict_collections

    cc = UICreator
    mouse_x,mouse_y = cc.mouse_xy(op)

    btn_title = cc.button(op, rectData=(mouse_x,mouse_y-50,200,50),text='DuplicateGrid')
    
    fv = FieldValue(
        value=(3, 3, 1),
        min=(0, 0, 0),
        max=(10, 10, 10),
        changeBy=(1, 1, 1)
    )
    
    vif_copies = cc.vectorIntField(op, btn_title.rectData.getBottom(5), fv, onCopiesChanged,
                                   parent=btn_title, canDrag=False)

    vff_translate = cc.vectorFloatField(op, vif_copies.rectData.getBottom(5), (2.0, 2.0, 2.0), placeObjects, parent=btn_title,canDrag=False)

    cb_distribution = cc.checkBox(op, vff_translate.rectData.getBottom(5), 'distribution', True, placeObjects, parent=btn_title,canDrag=False)  # True is step , false is range

    vbf_center = cc.vectorBooleanField(op, cb_distribution.button.rectData.getBottom(5), value=(True, True, True),
                                              onValueChange=placeObjects, parent=btn_title,canDrag=False)

    cb_inNewCollection = cc.checkBox(op, rectData=vbf_center.rectData.getBottom(5), text='new collection',
                                            ttt='Create objects in new collection',
                                            value=True, onValueChange=onNewCollectionChanged,parent=btn_title,canDrag=False)


    cb_collectionUnderScene = cc.checkBox(op, rectData=cb_inNewCollection.button.rectData.getBottom(5),
                                                 text='under the scene', value=False, ttt=ttt_under_scene,
                                                 onValueChange=onUnderSceneCollectionPressed,parent=btn_title,canDrag=False)


    

    total_copies = vif_copies.value[0] * vif_copies.value[1] * vif_copies.value[2]

    # create collections in the beginning

    dict_collections = {obj : getCollection(obj) for obj in objs}

    dict_createdObj.update({o: [] for o in objs})
    dict_objsToDelete.update({o: [] for o in objs})

    # Create new objects and link those to collection
    for (obj, coll), createdObjList in zip(dict_collections.items(), dict_createdObj.values()):
        for i in range(total_copies):
            ob = copyObj(obj, False, False, True)
            ob.name = obj.name + '_dupli_' + str(i)
            coll.objects.link(ob)
            createdObjList.append(ob)

    # place objects
    placeObjects()

    op.onCancel.append(cleanup)


