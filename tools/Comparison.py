from tools.selectFile import selectFile
import csv

def createListDomain(base, selectList):
    global NEW_DOMAIN, ALL_DOMAIN

    with open(base, 'r') as file:
        for row in csv.DictReader(file):
            domain = row['Domain']
            selectList.add(domain)



def ComparisonDomain():
    NEW_DOMAIN = set()
    ALL_DOMAIN = set()

    print('Select current base\n')
    tarFile = selectFile()
    print('\nSelect a common base\n')
    allBase = selectFile()
    print(tarFile)
    createListDomain(tarFile, NEW_DOMAIN)
    print(allBase)
    createListDomain(allBase, ALL_DOMAIN)
    
    number_domain = 0
    for domain in NEW_DOMAIN.intersection(ALL_DOMAIN):
        number_domain+=1
        print(f'[{number_domain}] {domain}')
