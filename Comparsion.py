from tools.selectFile import selectFile
from tools.RecordData import BASE_DIR
from tools.colors import GREEN, RESET
from tools.smallTools import customPath
import csv, os

def createListDomain(base, selectList):
    global NEW_DOMAIN, ALL_DOMAIN

    with open(base, 'r') as file:
        for row in csv.DictReader(file):
            domain = row['Domain']
            selectList.add(domain)


def recordComparison(path, name, email, job, company, domain, location, phone, linkedin, twitter, facebook):
    with open(path, 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, job, company, domain, location, phone, linkedin, twitter, facebook])


def ComparisonDomain():
    NEW_DOMAIN = set()
    ALL_DOMAIN = set()
    #Тут будут записаны домены после сравнения
    LIST_DOMAIN = set()
    pushinka = '-'*40
    print(f'{pushinka}\nSelect current base\n')
    tarFile = selectFile()
    print(f'{pushinka}\nSelect a common base\n')
    allBase = selectFile()
    createListDomain(tarFile, NEW_DOMAIN)
    createListDomain(allBase, ALL_DOMAIN)
    
    for domain in NEW_DOMAIN.intersection(ALL_DOMAIN):LIST_DOMAIN.add(domain)

    custom = customPath()
    print(custom)
    
    with open(allBase, 'r') as file:
        number = 0
        for row in csv.DictReader(file):
            email = row['Email']
            domain = row['Domain']
            name = row['Name']
            job = row['Job Title']
            company = row['Company']
            location = row['Location']
            phone = row['Phone']
            linkedin = row['Linkedin']
            twitter = row['Twitter']
            facebook = row['Facebook']
            if domain in LIST_DOMAIN:
                number+=1
                recordComparison(custom, name, email, job, company, domain, location, phone, linkedin, twitter, facebook)
                print(f'[{number}] Domain Recorded: {GREEN}{domain}{RESET}')
    


ComparisonDomain()
