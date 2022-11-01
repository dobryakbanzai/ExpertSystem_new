# чтение с бд
import csv
from collections import defaultdict
from csv import DictWriter

from Classes import Word


def read_info_from_bd():
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open('db.csv') as f:
        reader = csv.reader(f,delimiter=';')
        next(reader)
        for row in reader:
            for (i, v) in enumerate(row):
                if(v!=''):
                    columns[i].append(v)
        mylist = []
        for i in range(0, len(columns[0])):
            mylist.append(Word(columns[0][i],columns[1][i],'Северный'))

        for i in range(0, len(columns[2])):
            mylist.append(Word(columns[2][i],columns[3][i],'Центральный'))
        for i in range(0, len(columns[4])):
            mylist.append(Word(columns[4][i],columns[5][i],'Южный'))
    f.close()

    array=columns[0]+columns[2]+columns[4]
    return array, mylist


# Запись в бд
def writing_info_in_bd(word, array,mylist):

    with open('db.csv', 'a', newline='') as f:
        headersCSV = ['Северный-слово', 'Северный-значение', 'Центральный-слово', 'Центральный-значение', 'Южный-слово',
                      'Южный-значение']
        if word.getRegion()=='Северный':

            add_info('Северный',word,f,headersCSV)
            print('add '+ word.getMean())
        if word.getRegion()=='Центральный':
            add_info('Центральный',word, f, headersCSV)
            print('add '+ word.getMean())
        if word.getRegion()=='Южный':
            add_info('Южный',word,f,headersCSV)

    f.close()
    mylist.append(word)
    array.append(word)
    return array,mylist

def add_info(region,word,f,headerCSV):
    dictwriter_object = DictWriter(f, fieldnames=headerCSV,delimiter=';')
    dict = {region+'-слово':word.getWrd(), region+'-значение':word.getMean()}
    dictwriter_object.writerow(dict)

#