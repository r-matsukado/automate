from django.urls import path

from . import views

app_name = 'opefile'
urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/modal/init',views.ajaxInitForModal, name='ajaxInitForInit'),
    path('ajax/modal/file/exec',views.opeFileExec, name='opeFileExec'),
]