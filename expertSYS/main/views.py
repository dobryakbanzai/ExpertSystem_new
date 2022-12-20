import time

from django.views.generic import TemplateView
from Classes import Word
import WordSearch as ws
import WorkWithDatabase as wwd
from django.shortcuts import render
from django.shortcuts import HttpResponse
import MyMap as map
import main


def index(request):
    search_by = request.GET.get('search_by')
    if search_by == "reg":
        reg = request.GET.get('select')
        tag = 1
        if reg == "Северный":
            map.get_html_north()
            time.sleep(3)
        elif reg == "Южный":
            map.get_html_south()
            time.sleep(3)
        elif reg == "Центральный":
            map.get_html_avarage()
            time.sleep(3)
        elif reg == "Новый":
            map.get_html_new()
            time.sleep(3)
        else:
            map.get_html_all()
            time.sleep(3)
        if reg != "Всё":
            words = ws.get_all_wrd_in_reg(reg)
        else:
            tag = 0
            words = ws.get_all_wrd
    else:
        word = request.GET.get('query')
        tag = 0
        if word != '' and word != None:
            tag = 1
            words = ws.get_first_5(word)
            if words[0][2] == "Северный":
                map.get_html_north()
                time.sleep(3)
            elif words[0][2] == "Южный":
                map.get_html_south()
                time.sleep(3)
            elif words[0][2] == "Центральный":
                map.get_html_avarage()
                time.sleep(3)
            elif words[0][2] == "Новый":
                map.get_html_new()
                time.sleep(3)
            else:
                map.get_html_all()
                time.sleep(3)

        else:
            words = ws.get_all_wrd()
            map.get_html_all()
            time.sleep(3)

    return render(request, 'main/index.html', {'words': words, 'tag': tag})


def admin(request):
    h_ch = request.GET.get('h_ch')
    word = request.GET.get('word')
    mean = request.GET.get('mean')
    region = request.GET.get('region')
    n_d = request.GET.get('n_d')
    m_d = request.GET.get('m_d')
    s_d = request.GET.get('s_d')
    ne_d = request.GET.get('ne_d')

    word_send = ''
    checked_word = ''

    if n_d is not None:
        mean = mean + ' (' + n_d + ') '
    if m_d is not None:
        mean = mean + ' (' + m_d + ') '
    if s_d is not None:
        mean = mean + ' (' + s_d + ') '
    if ne_d is not None:
        mean = mean + ' (' + ne_d + ') '

    if h_ch is not None:
        word_send = Word(word, mean, region)
        checked_word = ws.get_first_5(word)[0]
    else:
        result = Word(word, mean, region)
        wwd.writing_info_in_bd(result)
    return render(request, 'main/admin.html', {'word': word_send, 'check': checked_word})


def logpas(request):
    return render(request, 'main/LogPas.html')