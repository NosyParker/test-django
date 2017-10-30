from django.conf.urls import url
from . import views

app_name = 'core_app'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/', views.system_sign_up, name='system_sign_up'),
]