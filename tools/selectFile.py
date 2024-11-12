import os
from tools.colors import RED, RESET, GREEN, YELLOW

def nextSelectStep(targetDir):
    number_file, counter_file, listFile = 0, 0, []
    for file in os.listdir(targetDir):
        if '.csv' in file:
            counter_file+=1
            listFile+=[file]
    
    if counter_file == 0:
        print(f'\n{RED}В {targetDir} нет файлов с базами{RESET}\n')
        selectFile()

    for file in listFile:
        number_file+=1
        print(f'{YELLOW}[{number_file}] {file}{RESET}\n')

    try:
        selectNumberFile = int(input(f'{GREEN}Select File: {RESET}'))
        selectElementFile = selectNumberFile-1
        targetFile = listFile[selectElementFile]
        print(f'\n{GREEN}File: {targetFile}{RESET}\n')
    except IndexError:nextSelectStep(targetDir)
    except ValueError:nextSelectStep(targetDir)
    except Exception as err:print(f'{RED}Error: {err}{RESET}')
    else:return f'{targetDir}/{targetFile}'

def selectFile():
    notIndexDir = ['tools', '.git', 'tmp']
    number_dir, listDir = 0, []
    for base_dir in os.listdir():
        if os.path.isdir(base_dir) and base_dir not in notIndexDir:
            listDir+=[base_dir]

    number_dir = 0
    for base_dir in listDir:
        number_dir+=1
        print(f'[{number_dir}] {base_dir}')

    try:
        selectDir = int(input(f'{GREEN}Select number DIR: {RESET}'))
        selectElementList = selectDir-1
        targetDir = listDir[selectElementList]
        print(f'\n{GREEN}Dir: {targetDir}{RESET}\n')
        return nextSelectStep(targetDir)
    except IndexError:
        selectFile()
    except Exception as err:print(f'{RED}Error: {err}{RESET}')
