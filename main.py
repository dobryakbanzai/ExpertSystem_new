# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import WorkWithDatabase as db
import Classes as ClassWord
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    db.create_bd()
    db.read_info_from_bd()
    db.writing_info_in_bd()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

words = ['aaa', 'bbb', 'ccc']
wordsClasses = [ClassWord.Word('aaa', 'aba', 'Nord'), ClassWord.Word('bbb', 'ass', 'ASsfa'), ClassWord.Word('ccc', 'asf', 'Afsaf')]

a = process.extractOne("abb", words)
print(a[0])

b = [x for x in wordsClasses if x.wrd == a[0]]
print(b[0].wrd, b[0].mean, b[0].region)
# wordsClassesindex(a[0])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
