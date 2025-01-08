import os, csv
from tools.selectFile import selectFile
from tools.colors import GREEN, RED, RESET
from tools.RecordData import BASE_DIR
from tools.smallTools import createHeader

DIR_MANY_BASE = 'Many'
LIST_BASE = []

def SearchBase():
    global LIST_BASE
    count_base, num_base = 0, 0
    try:
        for base in os.listdir(DIR_MANY_BASE):
            if '.csv' in base:
                count_base = 0
                num_base+=1
                LIST_BASE+=[base]
                count_base = num_base
                print(f'{RED}[{num_base}]{RESET}{GREEN}Base: {base}{RESET}')
    except FileNotFoundError as err:
        os.makedirs(DIR_MANY_BASE)
        print(f'{RED}No Base!{RESET}')
        count_base = 0

    print(f'{RED}Number of Bases: {count_base}{RESET}')

def Cleaning():
    global BASE_DIR, LIST_BASE
    clean_file = 'category_apollo.csv'
    path_clean_file = f'{BASE_DIR}/{clean_file}'
    SearchBase()

    if not os.path.exists(path_clean_file):createHeader(BASE_DIR, clean_file)
    if len(LIST_BASE) > 0:
        number_base, count_email = 0, 0
        for base in LIST_BASE:

            number_base+=1
            with open(f'{DIR_MANY_BASE}/{base}', 'r') as file:
                number_string=0
                
                for row in csv.DictReader(file):
                    try:
                        name = row['Name']
                        if '---' in name:
                            name = name.split('---')[0].strip()
                    except:name = 'N/A'
                    try:email = row['Email']
                    except:email = 'N/A'
                    try:job = row['Job Title']
                    except:job = 'N/A'
                    try:company = row['Company']
                    except:company = 'N/A'
                    try:domain = email.split('@')[1]
                    except:domain = 'N/A'
                    try:location = row['Location']
                    except:location = 'N/A'
                    try:phone = row['Phone']
                    except:phone = 'N/A'
                    try:linkedin = row['Linkedin']
                    except:linkedin = 'N/A'
                    try:twitter = row['Twitter']
                    except:twitter = 'N/A'
                    try:facebook = row['Facebook']
                    except:facebook = 'N/A'
                    try:category = row['Category']
                    except:category = 'N/A'
                    try:
                        if '@' in email and email:
                            number_string+=1
                            count_email+=1
                            with open(path_clean_file, 'a+') as file:
                                write = csv.writer(file)
                                write.writerow([name, email, job, company, domain, location, phone, linkedin, twitter, facebook, category])
                            print(f'{RED}[{number_base}][{number_string}]{RESET}{GREEN}[{count_email}] Name: {name}\tEmail: {email}\tDomain: {domain}{RESET}')
                    except:pass
                

    
Cleaning()
