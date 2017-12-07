from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core_app'
urlpatterns = [
     url (r'^$', views.HomeView.as_view(), name='home'),
     url (r'^sign-in/', views.logout_required(auth_views.login), 
        {"template_name":"core_app/sign_in.html"},
        name = "sign-in"),
     url (r'^sign-up/', views.logout_required(views.SignUpView.as_view()),
        name = "sign-up"),
     url (r'^logout/', auth_views.logout, 
        {"next_page":"/"},
        name = "logout"),
     url (r'^account/$', views.account, name="account"),
     url (r'^account/change-password/$', auth_views.password_change,
        {"post_change_redirect": "core_app:password_change_done","template_name":"core_app/change_password.html"}, name="change-password"),
     url (r'^account/change-password/done/$', auth_views.password_change_done,
        {"template_name":"core_app/password_change_done.html"}, name="password_change_done"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)