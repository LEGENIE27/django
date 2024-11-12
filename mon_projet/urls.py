from django.contrib import admin
from django.urls import path, include
from apk.views import home  # Importer la vue home
from apk.views import login 
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),  # Ajouter la route pour la racine
    path('', login, name='login'),
    path('apk/', include('apk.urls')),
]
