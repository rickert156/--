import csv, os
from tools.selectFile import selectFile
from tools.readBase import readBaseApollo, checkEmail, EMAIL_LIST
from tools.RecordData import BASE_FILE
from tools.smallTools import createHeader

def startBase():
    BASE = 'BaseAll'
    if not os.path.exists(f'{BASE}/{BASE_FILE}'):
        try:os.makedirs(BASE)
        except:pass
        createHeader(BASE, BASE_FILE)
    else:print(f'Директория {BASE} уже есть\n')


def main():
    file = selectFile()
    readBaseApollo(file)

if __name__ == '__main__':
    startBase()
    checkEmail()
    main()
