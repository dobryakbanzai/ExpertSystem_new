# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import WorkWithDatabase as db
from Classes import Word


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    all_words,words_info=db.read_info_from_bd()
    example=Word('Мансур','Салихов','Центральный')
    print(example.getMean())
    all_words,words_info=db.writing_info_in_bd(example,all_words,words_info)
    for x in range(len(words_info)):
        print(words_info[x].getWrd())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# wordsClassesindex(a[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
