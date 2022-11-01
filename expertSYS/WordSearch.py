import WorkWithDatabase as db
from Classes import Word
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import WordSearch as ws


def get_first_5(word):
    words_all, words_info = db.read_info_from_bd()
    result_simple = process.extract(word, words_all, limit=11)
    result = []
    for i in range(len(result_simple) - 1):
        b = [x for x in words_info if x.wrd == result_simple[i][0]]
        result.append((b[0].wrd, b[0].mean, b[0].region, result_simple[i][1]))
    return result


def get_all_wrd_in_reg(region):
    words_all, words_info = db.read_info_from_bd()
    result = []
    b = [x for x in words_info if x.region == region]
    for i in range(len(b) - 1):
        result.append((b[i].wrd, b[i].mean, b[i].region))
    return result


def get_all_wrd():
    words_all, words_info = db.read_info_from_bd()
    return words_info
