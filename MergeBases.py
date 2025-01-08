import csv, os
from tools.colors import RED, GREEN, BLUE, YELLOW, RESET

TARGET_DIR = 'Many'

ULTIMATE_DIR = 'General_Base'

SET_EMAIL = set()

def record_user(
        base_name:str=None, 
        name:str=None,
        email:str=None,
        job_title:str=None,
        company:str=None,
        location:str=None,
        phone:str=None,
        category:str=None):

    global ULTIMATE_DIR
    
    if base_name == None:base_name = 'Apollo.csv'

    if not os.path.exists(f'{ULTIMATE_DIR}/{base_name}'):
        with open(f'{ULTIMATE_DIR}/{base_name}', 'a') as file:
            write = csv.writer(file)
            write.writerow(['Name', 'Email', 'Job Title', 'Company', 'Location', 'Phone', 'Category'])

    with open(f'{ULTIMATE_DIR}/{base_name}', 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, job_title, company, location, phone, category])
    

def check_set_email(base_name:str=None):
    global ULTIMATE_DIR, SET_EMAIL
    
    if base_name == None:base_name = 'Apollo.csv'
    
    with open(f'{ULTIMATE_DIR}/{base_name}', 'r') as file:
        for row in csv.DictReader(file):
            email = row['Email']
            SET_EMAIL.add(email)




#Проверка наличия дирекотории, в которой будет несколько баз
def create_dir(target_dir:str=None):
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        
        #print(f'Директория {TARGET_DIR} создана, она пуста')
    

#Проверка баз в дирекотрии, где должны быть базы
def read_dir_base(target_dir:str=None):
    list_base = []
    #Добавление каждой базы в список баз
    for base in os.listdir(target_dir):
        list_base.append(base)

    return list_base
    

def read_each_base(target_dir:str=None):
    global SET_EMAIL

    #Создаем(если еще нету) директорию, где будет храниться баз
    create_dir(target_dir=ULTIMATE_DIR)
    
    #Собираем список баз, которые будем объединять
    list_base = read_dir_base(target_dir)
    
    """
    Читаем все базы через перебор for
    из каждой базы парсим нужные колонки
    """
    
    number_email = 0
    for base in list_base:
        with open(f'{target_dir}/{base}', 'r') as file:
           for row in csv.DictReader(file):
                
                try:
                    name = row['Name']
                    if '\n' in name:name = name.split('\n')[0]
                except:name='N/A'

                try:email = row['Email']
                except:email='N/A'
                
                try:job_title = row['Job Title']
                except:job_title='N/A'

                try:company = row['Company']
                except:company='N/A'

                try:location = row['Location']
                except:location='N/A'

                try:phone = row['Phone']
                except:phone='N/A'
                
                try:category = row['Category']
                except:category='N/A'
                

                if '@' in email and email not in SET_EMAIL:
                    number_email+=1
                    
                    
                    record_user(
                        name=name,
                        email=email,
                        job_title=job_title,
                        company=company,
                        location=location,
                        phone=phone,
                        category=category)
                    print(f'{YELLOW}[{number_email}]{RESET} Записан: {RED}{name}{RESET}\t{BLUE}{email}{RESET}')
                    #check_set_email()
                    

                

def MergeAllBase(target_dir:str=None):
    read_each_base(target_dir)
    



MergeAllBase(target_dir=TARGET_DIR)
