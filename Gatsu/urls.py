from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, RecientesView, TopMangasView, SobreGatsuView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Home.html', HomeView.as_view(), name='home'),
    path('Recientes.html', RecientesView.as_view(), name='recientes'),
    path('TopMangas.html', TopMangasView.as_view(), name='TopMangas'),
    path('SobreGatsu.html', SobreGatsuView.as_view(), name='SobreGatsu'),
    path('', HomeView.as_view(), name='default'),  # Ruta para la página por defecto
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)