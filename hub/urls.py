from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^panel/([0-9]+)/$', views.panel, name='panel'),
    url(r'^register/$', views.register, name='register'),
    url(r'login/', csrf_exempt(views.login), name='login'),
    url(r'logout/', views.logout, name='logout'),
    url(r'success/', views.success, name='success'),
    url(r'failure/', views.failure, name='failure'),
    url(r'upload/',  csrf_exempt(views.upload_file), name='upload'), #need csrf exempt to prevent HTTP 302
    url(r'([a-zA-Z0-9]+)/repos/(.+)/$', views.repo, name='repo'),
    url(r'([a-zA-Z0-9]+)/repos/(.+)/(.+)$', views.repoFiles, name='repoCommit')
   # url(r'uploads/', views.render_file, name='show_file')
]