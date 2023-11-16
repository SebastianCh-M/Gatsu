from django.contrib import admin
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from .models import tipoEstado, tipoSubida, Manga3, Usuario, Administrador, MangaGatsu, Capitulo, Imagen, RegistroPago, Comentario, Valoracion, Revista, NombreManga, Revista2
from django.utils.safestring import mark_safe
=======
from .models import tipoEstado, tipoSubida, Manga3, SetImagen
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)
=======
from .models import tipoEstado, tipoSubida, Manga3, SetImagen
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)
=======
from .models import tipoEstado, tipoSubida, Manga3, SetImagen
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)

# Register your models here.

class subidaAdmin(admin.ModelAdmin):
    list_display=["subida"]

class estadoAdmin(admin.ModelAdmin):
    list_display=["estado"]

class mangaAdmin(admin.ModelAdmin):
    list_display=['idManga', 'nombreManga', 'ano_publicacion','tsubida','mangaka','sinopsis','editorial','genero','estado','imagen']    

class imagenAdmin(admin.ModelAdmin):
    list_display=['idLote','capitulo','manga','grupoImagen']    
<<<<<<< HEAD
<<<<<<< HEAD

class editorialAdmin(admin.ModelAdmin):
    list_display = ["editorial_id","editoriales"]    

admin.site.register(Revista2, editorialAdmin)    
=======
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)
=======
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)




#-------------Registro----------------------

admin.site.register(tipoSubida, subidaAdmin)
admin.site.register(tipoEstado, estadoAdmin)     
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
admin.site.register(Manga3)
admin.site.register(Revista)  # Registrar la tabla Revista

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'correo')

@admin.register(MangaGatsu)
class MangaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_manga', 'anio_publicacion', 'tipo_subida', 'get_revista', 'genero', 'estado', 'portada')
    list_filter = ('estado', 'genero')

    def get_revista(self, obj):
        return obj.nombre_manga.revista.editoriales

    get_revista.short_description = 'Revista'

@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = ('id', 'capitulo', 'show_image')

    def show_image(self, obj):
        return mark_safe(f'<img src="{obj.imagen.url}" style="max-height:100px;max-width:100px;" />')

    show_image.allow_tags = True
    show_image.short_description = 'Imagen'

@admin.register(Capitulo)
class CapituloAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'numero', 'fecha_publicacion', 'manga')

    def __str__(self):
        return f"Capítulo {self.numero} - {self.titulo}"


@admin.register(RegistroPago)
class RegistroPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_usuario', 'usuario')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'contenido', 'fecha_hora', 'usuario', 'capitulo')

@admin.register(Valoracion)
class ValoracionAdmin(admin.ModelAdmin):
    list_display = ('id', 'valoracion', 'usuario', 'manga')

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_registro', 'correo')

@admin.register(NombreManga)
class NombreMangaAdmin(admin.ModelAdmin):
    list_display = ('id', 'revista', 'nombreManga', 'mangaka')
=======
admin.site.register(Manga3, mangaAdmin)
admin.site.register(SetImagen, imagenAdmin)
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)
=======
admin.site.register(Manga3, mangaAdmin)
admin.site.register(SetImagen, imagenAdmin)
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)
=======
admin.site.register(Manga3, mangaAdmin)
admin.site.register(SetImagen, imagenAdmin)
>>>>>>> parent of 0db9525 (Merge pull request #97 from SebastianCh-M/main)
