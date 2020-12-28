from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.index_page, name='index_page'),
    path('<str:id>', views.index_str, name='index_str'),
]

