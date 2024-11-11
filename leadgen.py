import csv, os
from tools.selectFile import selectFile
from tools.readBase import readBaseApollo, checkEmail, EMAIL_LIST
from tools.RecordData import BASE_FILE
from tools.Comparison import ComparisonDomain
           
def startBase():
    t = "Email,Name,Job Title,Company,Domain,Location,Phone,Linkedin,Twitter,Facebook"
    BASE = 'BaseAll'
    if not os.path.exists(BASE):
        os.makedirs(BASE)
        print(f'Директория {BASE} создана\n')
        os.system(f'echo {t} > {BASE}/{BASE_FILE}')
    else:print(f'Директория {BASE} уже есть\n')


def main():
    file = selectFile()
    readBaseApollo(file)

if __name__ == '__main__':
    startBase()
    checkEmail()
    #main()
    ComparisonDomain()
