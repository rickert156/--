import csv, os
from tools.colors import RESET, RED

BASE_DIR = 'BaseAll'
BASE_FILE = 'apollo.csv'

def recordBase(name, email, job, company, domain, location, phone, linkedin, twitter, facebook, category):
    global BASE_DIR, BASE_FILE

    targenFile = f'{BASE_DIR}/{BASE_FILE}'
    with open(targenFile, 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, job, company, domain, location, phone, linkedin, twitter, facebook, category])
        print(f'Email recorded: {RED}{email}{RESET}')

