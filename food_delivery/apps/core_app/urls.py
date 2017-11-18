from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

app_name = 'core_app'
urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'^sign-in/', views.logout_required(auth_views.login), 
        {"template_name":"core_app/sign_in.html"},
        name = "sign-in"),
     url(r'^sign-up/', views.logout_required(views.sign_up),
        name = "sign-up"),
     url(r'^logout/', auth_views.logout, 
        {"next_page":"/"},
        name = "logout"),
     url (r'^account/$', views.account, name="account"),
     url (r'^account/change-password/$', auth_views.password_change,
        {"post_change_redirect":"core_app/account.html"}, name="change-password")

]