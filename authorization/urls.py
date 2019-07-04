from django.conf.urls import url
from . import views

app_name = 'authorization'
urlpatterns = [
    url(r'^$', views.personalpage_login, name='login'),
    url(r'^logout$', views.personalpage_logout, name='logout'),
]