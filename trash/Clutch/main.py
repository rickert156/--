import csv, os

LIST_BASE = []
NEW_BASE = 'Clutch.csv'

def recordBase(name, email, domain, company):
    if not os.path.exists(NEW_BASE):
        with open(NEW_BASE, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Name', 'Email', 'Domain', 'Company'])

    with open(NEW_BASE, 'a+') as file:
        write = csv.writer(file)
        write.writerow([name, email, domain, company])


def readBase():
    global LIST_BASE

    for base in LIST_BASE:
        number_email = 0
        with open(base, 'r') as file:
            for row in csv.DictReader(file):
                number_email+=1
                name = row['Name']
                email = row['Email']
                domain = row['Domain']
                company = row['Company']
                recordBase(name, email, domain, company)
                print(f'\t[{number_email}] {email}\t{company}')



def main():
    global LIST_BASE
    number_base = 0
    for base in os.listdir():
        if '.csv' in base:
            number_base+=1
            LIST_BASE+=[base]
            print(f'[{number_base}] Add {base}')

    readBase()


main()

