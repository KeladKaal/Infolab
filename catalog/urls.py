from django.conf.urls import url
from django.urls import path, reverse_lazy, include

from . import views


app_name = 'catalog'
urlpatterns = [


   # # ex: /catalog/5/
   #
    # ex: /polls/5/results/
   # path(r'^(?P<clubs_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
  #  path(r'^(?P<clubs_id>[0-9]+)/vote/$', views.vote, name='vote'),
    path('detail/<int:clubs_id>', views.detail, name="detail"),
    path('show_clubs/', views.show_clubs, name='show_clubs'),
    path('wow/', views.wow, name='wow'),
    path('register/', views.register, name='register')]

