from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from .views import HomeView, RecientesView, TopMangasView, SobreGatsuView, MiBibliotecaView, RecuperarView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name = "home"),
    path('home', HomeView.as_view(), name='home'),
    path('recientes', RecientesView.as_view(), name='recientes'),
    path('top-mangas', TopMangasView.as_view(), name='top-mangas'),
    path('sobre-gatsu', SobreGatsuView.as_view(), name='sobre-gatsu'),
    path('mi-biblioteca', MiBibliotecaView.as_view(), name='mi-biblioteca'),
    path('Recuperar', RecuperarView.as_view(), name='Recuperar'),
    path('manga/', include('manga.urls')),
    
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


