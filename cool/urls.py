
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static         # in these url page also we add static

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:cools_id>', views.detail, name='detail'),     # it can read user's id one by one
    path('<int:cools_id>/upvote', views.upvote, name='upvote')
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 