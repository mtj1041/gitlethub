from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^panel/([0-9]+)/$', views.panel, name='panel'),
    url(r'^register/$', views.register, name='register'),
]