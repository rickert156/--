import csv, os
from tools.selectFile import selectFile
from tools.readBase import readBaseApollo, checkEmail, EMAIL_LIST
from tools.RecordData import BASE_FILE
           
def startBase():
    BASE = 'BaseAll'
    if not os.path.exists(BASE):
        os.makedirs(BASE)
        with open(f'{BASE}/{BASE_FILE}', 'a') as file:
            write = csv.writer(file)
            write.writerow(['Email', 'Job Title', 'Company', 'Domain', 'Location', 'Phone', 'Linkedin', 'Twitter', 'Facebook'])
    else:print(f'Директория {BASE} уже есть\n')


def main():
    file = selectFile()
    readBaseApollo(file)

if __name__ == '__main__':
    startBase()
    checkEmail()
    main()
