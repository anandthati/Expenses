from django.conf import settings
from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import logout, login

regex = '[\w!@#$%^&*()+,.;:\'"-_ ]' #pylint: disable=anomalous-backslash-in-string
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login,{'template_name':'login.html'}, name='login'),
    url(r'^logout/$', logout,{'next_page':'index'}, name='logout'),
    url(r'^singup$', views.register, name='signupform'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^summary$', views.summary, name='summary'),
    url(r'^addexpense$', views.addexpense, name='addexpense'),
    url(r'^addincome$', views.addincome, name='addincome'),
    ]
