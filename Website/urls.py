from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^main/$', views.main, name='main2'),
    url(r'^main/#serve$', views.main, name='mainpred'),
    url(r'^about/$', views.about, name='about'),
    url(r'^first_inn/$', views.first_inn, name='first_inn'),
    url(r'^second_inn/$', views.second_inn, name='second_inn'),
    url(r'^pre_pred/$', views.prematch, name='prematch'),
]
