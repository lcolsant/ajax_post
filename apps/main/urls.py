from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_post$', views.add_post),
    url(r'^get_post$', views.get_post),
    url(r'^delete/(?P<id>\d+)$', views.delete),
]