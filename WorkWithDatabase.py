# чтение с бд
import csv
from collections import defaultdict

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
            mylist.append(Word(columns[2][i],columns[1][i],'Центральный'))

        for i in range(0, len(columns[4])):
            mylist.append(Word(columns[4][i],columns[1][i],'Южный'))


    array=columns[0]+columns[2]+columns[4]

    for x in range(len(mylist)):
        print (mylist[x].getWrd())
    return array,mylist

# Запись в бд
def writing_info_in_bd(word, array,mylist):
    if word.getRegion()=='Северный':
        print()
    if word.getRegion()=='Центральный':
        print()
    if word.getRegion()=='Южный':
        print()

    mylist.append(word.getWrd,word.getMean(),word.getRegion())
    array.append(word)
    return array,mylist
#