from django.urls import path

from . import views

urlpatterns = [
    path('<str:serial>', views.provision, name='provision')
]