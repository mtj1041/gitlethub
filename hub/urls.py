from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^panel/([0-9]+)/$', views.panel, name='panel'),
    url(r'^register/$', views.register, name='register'),
    url(r'login/', views.login, name='login'),
    url(r'logout/', views.logout, name='logout'),
    url(r'success/', views.success, name='success'),
    url(r'failure/', views.failure, name='failure'),
    url(r'upload/', views.upload_file, name='upload')
]