from django import forms

from .models import Post, Manga3, SetImagen

# pip install django-multiupload
from multiupload.fields import MultiFileField


class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')

class mangaForm(forms.ModelForm):
    class Meta:
        model = Manga3
        fields = ['idManga', 'nombreManga', 'ano_publicacion','tsubida','mangaka','sinopsis','editorial','genero','estado','imagen'] 

       


class imagenForm(forms.ModelForm):
    class Meta:
        model = SetImagen    
        fields = ['idLote', 'capitulo', 'manga','grupoImagen']

        



class imagenForm2(forms.ModelForm):     
        idLote = forms.CharField(max_length=255)
        capitulo = forms.CharField(max_length=255)
        manga = forms.ModelChoiceField(queryset=Manga3.objects.all())       
        grupoImagen = MultiFileField(min_num=1, max_num=10)
