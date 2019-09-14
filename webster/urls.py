
from django.contrib import admin
from django.urls import path, include               # it can include a file of accounts app
from cool import views                              # allow to access views from cool app
from django.conf import settings
from django.conf.urls.static import static          # support static files


urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('cool/', include('cool.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
