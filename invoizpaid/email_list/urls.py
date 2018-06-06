from django.conf.urls import url
from email_list import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^list/$', views.list),
    url(r'^add/$', views.add),
]