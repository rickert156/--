import os, csv

BASE_FILE = 'Clutch.csv'

def divideBase(number_email, company, email, name):
    filename = f'{number_email}.csv'
    if not os.path.exists(filename):
        with open(filename, 'a') as file:
            write = csv.writer(file)
            write.writerow(['Company', 'Email', 'Name'])

    with open(filename, 'a+') as file:
        write = csv.writer(file)
        write.writerow([company, email, name])

def main():
    global BASE_FILE

    with open(BASE_FILE, 'r') as file:
        number_email = 0
        for row in csv.DictReader(file):
            number_email+=1
            name = row['Name']
            email = row['Email']
            company = row['Company']
            print(f'[{number_email}] {email} {company}')
            divideBase(number_email, company, email, name)
            if number_email == 3:number_email = 0

main()
