from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from manga.views import registrarManga, manga_list
from .views import HomeView, LoginView, RecientesView, TopMangasView, SobreGatsuView, MiBibliotecaView, RecuperarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login', LoginView.as_view(), name="login"),
    path('Home', HomeView.as_view(), name='home'),
    path('Recientes', RecientesView.as_view(), name='recientes'),
    path('TopMangas', TopMangasView.as_view(), name='TopMangas'),
    path('SobreGatsu', SobreGatsuView.as_view(), name='SobreGatsu'),
    path('MiBiblioteca', MiBibliotecaView.as_view(), name='MiBiblioteca'),
    path('Recuperar', RecuperarView.as_view(), name='Recuperar'),
    path('', HomeView.as_view(), name='default'),  # Ruta para la página por defecto
    path('manga_create', registrarManga),
    path('manga_list', manga_list)
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)