from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static
from manga.views import formRevista, listaRevista, deleR, updaR, formNombreManga, listaNombreManga, deleN, updaN, formMangaGatsu, listaMangaGatsu, deleM, updaM, formCapitulo, listaCapitulo, deleC, updaC, formImagen, listaImagen, deleI, updaI
from .views import HomeView, RecientesView, TopMangasView, SobreGatsuView, MiBibliotecaView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view(), name = "home"),
<<<<<<< HEAD
    path('Home', HomeView.as_view(), name='Home'),
    path('Recientes', RecientesView.as_view(), name='Recientes'),
=======
    path('login.html', LoginView.as_view(), name="login"),
    path('Home', HomeView.as_view(), name='home'),
<<<<<<< HEAD
    path('Recientes', RecientesView.as_view(), name='recientes'),
>>>>>>> parent of da5250f (pequeño commit)
    path('TopMangas', TopMangasView.as_view(), name='TopMangas'),
    path('SobreGatsu', SobreGatsuView.as_view(), name='SobreGatsu'),
    path('MiBiblioteca', MiBibliotecaView.as_view(), name='MiBiblioteca'),
    path('', HomeView.as_view(), name='default'),  # Ruta para la página por defecto
<<<<<<< HEAD

    #Revisa
    path('formRevista',formRevista),
    path('listaRevista',listaRevista),
    path('deleR/<int:id>', deleR),
    path('updaR/<int:id>', updaR),

    #Nombre Manga
    path('formNombreManga',formNombreManga),
    path('listaNombreManga',listaNombreManga),
    path('deleN/<int:id>', deleN),
    path('updaN/<int:id>', updaN),

    #Manga Gatsu
    path('formMangaGatsu',formMangaGatsu),
    path('listaMangaGatsu',listaMangaGatsu),
    path('deleM/<int:id>', deleM),
    path('updaM/<int:id>', updaM),

    #Capitulo
    path('formCapitulo',formCapitulo),
    path('listaCapitulo',listaCapitulo),
    path('deleC/<int:id>', deleC),
    path('updaC/<int:id>', updaC),

    #Imagen
    path('formImagen',formImagen),
    path('listaImagen',listaImagen),
    path('deleI/<int:id>', deleI),
    path('updaI/<int:id>', updaI),






    #path('delete_revista/<int:revista_id>', delete_Revista),
    #path('eliminarR/<int:pk>', eliminarRevista),
    #path('manga_create', registrarManga),
    #path('manga_list', manga_list),
    #path('capitulos_form',registrarImagenes)
=======
    path('manga_create', registrarManga),
    path('manga_list', manga_list),
    path('capitulos_form',registrarImagenes)
=======
    path('Recientes.html', RecientesView.as_view(), name='recientes'),
    path('TopMangas.html', TopMangasView.as_view(), name='TopMangas'),
    path('SobreGatsu.html', SobreGatsuView.as_view(), name='SobreGatsu'),
    path('MiBiblioteca.html', MiBibliotecaView.as_view(), name='MiBiblioteca'),
    path('Recuperar.html', RecuperarView.as_view(), name='Recuperar'),
    path('Home.html', HomeView.as_view(), name='home'),  # Ruta para la página por defecto
    path('manga_create.html', registrarManga),
    path('manga_list.html', manga_list),
>>>>>>> 3f0c3e9e3b892dea795a430e815d05c7044d56e9
>>>>>>> parent of da5250f (pequeño commit)
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


