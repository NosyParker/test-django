from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'core_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^sign-up/$', views.system_sign_up, name='system_sign_up'),
    url(r'^sign-in/$', views.ELoginView.as_view(), name='system_sign_in'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'core_app/logged_out.html'}, name='system_logout'),
]