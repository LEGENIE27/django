from django.contrib import admin
from django.urls import path, include
from apk.views import home  # Importer la vue home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),  # Ajouter la route pour la racine
    path('apk/', include('apk.urls')),
]
