# чтение с бд
import csv
from collections import defaultdict
from csv import DictWriter

from Classes import Word


def read_info_from_bd():
    columns = defaultdict(list)  # each value in each column is appended to a list
    with open('db.csv') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            for (i, v) in enumerate(row):
                if (v != ''):
                    columns[i].append(v)
        mylist = []

        for i in range(0, len(columns[0])):
            mylist.append(Word(columns[0][i], columns[1][i], 'Стекольный отдел'))
        for i in range(0, len(columns[2])):
            mylist.append(Word(columns[2][i], columns[3][i], 'Отдел корпусов'))
        for i in range(0, len(columns[4])):
            mylist.append(Word(columns[4][i], columns[5][i], 'Топливный отдел'))

    f.close()

    array = columns[0] + columns[2] + columns[4] + columns[6] + columns[8]
    return array, mylist


# Запись в бд
def writing_info_in_bd(word):
    with open('db.csv', 'a', newline='') as f:
        headersCSV = ['Стекольный отдел-слово', 'Стекольный отдел-значение', 'Отдел корпусов-слово', 'Отдел корпусов-значение', 'Топливный отдел-слово',
                      'Топливный отдел-значение']

        if word.getRegion() == 'Стекольный отдел':
            add_info('Стекольный отдел', word, f, headersCSV)
        if word.getRegion() == 'Отдел корпусов':
            add_info('Отдел корпусов', word, f, headersCSV)
        if word.getRegion() == 'Топливный отдел':
            add_info('Топливный отдел', word, f, headersCSV)

    f.close()
    return


def add_info(region, word, f, headerCSV):
    dictwriter_object = DictWriter(f, fieldnames=headerCSV, delimiter=';')
    dict = {region + '-слово': word.getWrd(), region + '-значение': word.getMean()}
    dictwriter_object.writerow(dict)

#