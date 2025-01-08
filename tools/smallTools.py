import os, csv

def customPath():
    newResultDir = input('Input dir: ')
    newResultFile = input('Input file: ')
    
    if not os.path.exists(newResultDir):os.makedirs(newResultDir)
    if '.csv' not in newResultFile:newResultFile = f'{newResultFile}.csv'
    resultCustomPath = f'{newResultDir}/{newResultFile}'

    return resultCustomPath

def createHeader(base, target_file):
    with open(f'{base}/{target_file}', 'a') as file:
        write = csv.writer(file)
        write.writerow(['Name', 'Email', 'Job Title', 'Company', 'Domain', 'Location', 'Phone', 'Linkedin', 'Twitter', 'Facebook', 'Category'])

