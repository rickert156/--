import csv, os
from tools.colors import RED, RESET, GREEN, YELLOW

SET_EMAIL = set()

SET_DOMAIN = set()


#Читаем базу имейлов
def read_base_email(path_base):
    global SET_EMAIL

    with open(path_base, 'r') as file:
        for row in csv.DictReader(file):
            email = row['Email']
            SET_EMAIL.add(email)


#Читаем базу доменов
def read_base_domain(path_domain_base):
    global SET_DOMAIN

    with open(path_domain_base, 'r') as file:
        for row in csv.DictReader(file):
            domain = row['Domain']

            if 'http' in domain:domain = domain.split('//')[1]
            if '@' in domain:domain = domain.split('@')[1]

            SET_DOMAIN.add(domain)


def record_email_new_base(
        new_base_file:str=None,
        name:str=None,
        email:str=None,
        job_title:str=None,
        company:str=None,
        location:str=None,
        domain:str=None,
        category:str=None):

    result_dir = 'Result'
    if new_base_file == None: new_base_file = 'result_search_lead_by_domain.csv'

    if not os.path.exists(result_dir):os.makedirs(result_dir)

    path_file_result = f'{result_dir}/{new_base_file}'
    if not os.path.exists(path_file_result):
        with open(path_file_result, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Name', 'Email', 'Job Title', 'Company', 'Location', 'Domain', 'Category'])

    with open(path_file_result, 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, job_title, company, location, domain, category])

    
def Collector(path_base):
    with open(path_base, 'r') as file:
        number_email = 0
        for row in csv.DictReader(file):
            name = row['Name']
            email = row['Email']
            job_title = row['Job Title']
            company = row['Company']
            location = row['Location']
            category = row['Category']
            
            domain = email.split('@')[1]

            if domain in SET_DOMAIN:
                number_email+=1
                record_email_new_base(
                        name=name,
                        email=email,
                        job_title=job_title,
                        company=company,
                        location=location,
                        domain=domain,
                        category=category)
                print(f'{YELLOW}[{number_email}]{RESET} {GREEN}{name}\t{email} {company}{RESET}')
             




def Search_Lead(dir_base:str, base:str, dir_base_domain:str, domain_file:str):
    path_base = f'{dir_base}/{base}'
    path_domain_base = f'{dir_base_domain}/{domain_file}'

    read_base_email(path_base)
    read_base_domain(path_domain_base)
    
    Collector(path_base)


Search_Lead(
        dir_base='General_Base', 
        base='Apollo.csv',
        dir_base_domain='TargetBase',
        domain_file='y_comb.csv')
