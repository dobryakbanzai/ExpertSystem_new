from django.urls import path
from . import views
# from .. import WordSearch

urlpatterns = [
    path('', views.index),
    path('manage/', views.admin),
    # path('checker/', WordSearch.get_first_5)
    # path('conf/', views.confirmation)
]
