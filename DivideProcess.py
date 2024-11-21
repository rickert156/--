import csv, os, time
from tools.colors import RED, GREEN,YELLOW, RESET

def Description():
    description = f"""{RED}
    Это скрипт для обработки промежуточного результата
    парсера apollo. В FirstStepApolloBetter скопированы 
    базы с машин, что бы можно было их пересобрать и перераспределить
    {RESET}
    """
    print(description)

BASE_DIR = 'FirstStepApolloBetter'
FULL_BASE = 'full_base.csv'

SET_LINK = set()

def checkFullBase(path):
    if not os.path.exists(path):
        with open(path, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Domain', 'Link'])

def recordingData(domain, link):
    global BASE_DIR, FULL_BASE, SET_LINK
    path_full_base = f'{BASE_DIR}/{FULL_BASE}'
    checkFullBase(path_full_base)

    
    with open(path_full_base, 'a+') as file:
        write = csv.writer(file)
        write.writerow([domain, link])

def ProcessingFile(path):
    with open(path, 'r') as file:
        number_string = 0
        for row in csv.DictReader(file):
            number_string+=1
            domain = row['Domain']
            link = row['Link']
            recordingData(domain, link)
            print(f'\t[x {GREEN}{number_string}{RESET} x] {GREEN}{domain}{RESET} | {YELLOW}{link}{RESET}')


def checkBase():
    global BASE_DIR, FULL_BASE
    if os.path.exists(BASE_DIR):
        number_base = 0
        for base in os.listdir(BASE_DIR):
            if base != FULL_BASE:
                number_base+=1
                base_path = f'{BASE_DIR}/{base}'
                print(f'[{number_base}] Procesing base {base}...')
                time.sleep(1)
                ProcessingFile(base_path)
    
    else:
        os.makedirs(BASE_DIR)
        print(f'Директории {BASE_DIR} не была создана ранее!\nСейчас дирекотрия {BASE_DIR} создана. Загрузите туда базы.')

def createNewFile(fileName):
    global BASE_DIR
    target_file = f'{BASE_DIR}/{fileName}'
    if not os.path.exists(target_file):
        with open(target_file, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Domain', 'Link'])

def divideFile(fileName, domain, link):
    global BASE_DIR
    createNewFile(fileName)

    with open(f'{BASE_DIR}/{fileName}', 'a+') as file:
        write = csv.writer(file)
        write.writerow([domain, link])

def Divide(num):
    global BASE_DIR, FULL_BASE
    path_full_base = f'{BASE_DIR}/{FULL_BASE}'
    with open(path_full_base, 'r') as file:
        number_link = 0
        for row in csv.DictReader(file):
            number_link+=1
            domain = row['Domain']
            link = row['Link']
            fileNew = f'domain_{number_link}.csv'
            print(f'{domain} | {link} >> {fileNew}')
            divideFile(fileNew, domain, link)
            if number_link >= num:number_link = 0



def DivideProcess():
    #Description() # Для сборки  
    #checkBase()   # в один файл
    
    Divide(4) # разделяем на файлы
    

if __name__ == '__main__':
    DivideProcess()

