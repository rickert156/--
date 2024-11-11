import csv
from tools.RecordData import recordBase
from tools.RecordData import BASE_DIR, BASE_FILE

EMAIL_LIST = []

def checkEmail():
    global EMAIL_LIST
    
    targenFile = f'{BASE_DIR}/{BASE_FILE}'
    with open(targenFile, 'r') as file:
        print('Start reading the database...')
        for row in csv.DictReader(file):
            email = row['Email']
            EMAIL_LIST+=[email]
        print('Finish reading the database!\n')

def readBaseApollo(selectFile):
    global EMAIL_LIST

    with open(selectFile, 'r') as file:
        number_email, counter_email = 0, 0
        for row in csv.DictReader(file):
            counter_email = 0
            number_email+=1
            email = row['Email']
            name = row['Name']
            job = row['Job Title']
            company = row['Company']
            location = row['Location']
            phone = row['Phone']
            linkedin = row['Linkedin']
            twitter = row['Twitter']
            facebook = row['Facebook']
            if '@' in email:domain = email.split('@')[1]
            else:domain = 'Not Defined'
            counter_email=number_email 
            print(f'[{number_email}] {email} | {name} {company}({domain})')
            if email not in EMAIL_LIST:
                recordBase(email, name, job, company, domain, location, phone, linkedin, twitter, facebook)
        print(f'Всего имейлов: {counter_email}')

 
