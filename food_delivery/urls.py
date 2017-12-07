from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('core_app.urls',namespace = "core_app")),
    url(r'^cart/', include('cart.urls', namespace = "cart")),
]
