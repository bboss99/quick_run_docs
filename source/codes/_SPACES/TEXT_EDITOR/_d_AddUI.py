import bpy
from boss.utils import getFileList
from os.path import dirname, join

def getCodeTTT(caller):
    with open(caller.param) as f:
        lines = f.read().splitlines()
    return lines


def getCodeLines(filePath):
    with open(filePath) as f:
        lines = f.read().splitlines()
    return lines

def getCode(filePath):
    with open(filePath, 'r') as file:
        data = file.read()
    return data

def paste_code(caller):
    curText = bpy.context.space_data.text

    if curText:
        spaceFromLeft = curText.current_character
        start_line_index = curText.current_line_index

        for i, line in enumerate(getCodeLines(caller.param)):
            if i == 0:
                curText.write(line + '\n')
            else:
                curText.cursor_set(start_line_index)
                curText.write(' '*spaceFromLeft + line + '\n')
            start_line_index +=1

        curText.cursor_set(start_line_index,character=spaceFromLeft)

def get_sub_md():
    # texts, onClicks, toolTipTexts,toolTipImages, get_submenu_data_fns,params

    dir_codesPath = join(dirname(__file__),"_add_ui_files" )

    codeFileNames = getFileList(dir_codesPath)
    codeFilePaths = [join(dir_codesPath,f) for f in codeFileNames]

    cnt = len(codeFileNames)
    return codeFileNames, [paste_code]*cnt, [getCodeTTT]*cnt,\
           ['']*cnt, [None]*cnt, codeFilePaths
