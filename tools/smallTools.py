import os

def customPath():
    newResultDir = input('Input dir: ')
    newResultFile = input('Input file: ')
    
    if not os.path.exists(newResultDir):os.makedirs(newResultDir)
    if '.csv' not in newResultFile:newResultFile = f'{newResultFile}.csv'
    resultCustomPath = f'{newResultDir}/{newResultFile}'

    return resultCustomPath


