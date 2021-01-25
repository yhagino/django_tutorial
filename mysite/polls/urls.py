from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.index_page, name='index_page'),
    path('<str:id>', views.index_str, name='index_str'),
    path('<int:question_id>/', views.detail, name='detail'),  # ex: /polls/5/
    path('<int:question_id>/results/', views.results, name='results'),  # ex: /polls/5/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),  # ex: /polls/5/vote/
]
