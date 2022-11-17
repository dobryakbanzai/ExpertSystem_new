from django.views.generic import TemplateView

import WordSearch as ws
import WorkWithDatabase as wwd
from django.shortcuts import render
from django.shortcuts import HttpResponse
import main


# Create your views here.
# class HomePageView(TemplateView):
#     template_name = "main/index.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         search_by = self.request.GET.get('search_by')
#
#         return context

def index(request):
    search_by = request.GET.get('search_by')
    if search_by == "reg":
        reg = request.GET.get('select')
        tag = 1
        words = ws.get_all_wrd_in_reg(reg)
    else:
        word = request.GET.get('query')
        tag = 0
        if word != '' and word != None:
            tag = 1
            words = ws.get_first_5(word)
        else:
            words = ws.get_all_wrd()

    return render(request, 'main/index.html', {'words': words, 'tag': tag})

# def postuser(request):
#
#     words = ws.get_first_5(searcher)
#     return render(request, 'main/index.html', {'words': words})
