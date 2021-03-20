import bpy
from boss.utils import getFileList
from os.path import dirname, join,basename
from boss_quick_run.Q import getCode as QGetCode

def getCodeTTT(caller):
    return QGetCode(caller.param)


def getCode(filePath):
    with open(filePath, 'r') as file:
        data = file.read()
    return data


def create_text_data(caller):
    t = bpy.data.texts.new(basename(caller.param))
    t.write(getCode(caller.param))
    bpy.context.space_data.text = t
    caller.op.quit()

 
def get_sub_md():
    # texts, onClicks, toolTipTexts,toolTipImages, get_submenu_data_fns,params

    dir_codesPath = join(dirname(__file__),"_add_presets_files" )

    codeFileNames = getFileList(dir_codesPath)
    codeFilePaths = [join(dir_codesPath,f) for f in codeFileNames]
    cnt = len(codeFileNames)
    return codeFileNames, [create_text_data]*cnt, [getCodeTTT]*cnt,\
           ['']*cnt, [None]*cnt, codeFilePaths
