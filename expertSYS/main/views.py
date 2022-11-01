import WordSearch as ws
import WorkWithDatabase as wwd
from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.


def index(request):
    words = ws.get_all_wrd()
    return render(request, 'main/index.html', {'words': words})


# def postuser(request):
#
#     words = ws.get_first_5(searcher)
#     return render(request, 'main/index.html', {'words': words})
