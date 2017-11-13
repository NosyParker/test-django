from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core_app'
urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^sign-in/', auth_views.login, 
        {"template_name":"core_app/sign_in.html"},
        name = "sign-in"),
     url(r'^sign-up/', views.sign_up,
        name = "sign-up"),
     url(r'^logout/', auth_views.logout, 
        {"next_page":"/"},
        name = "logout"),
]