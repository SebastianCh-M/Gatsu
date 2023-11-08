from django import forms

from .models import Post, Manga3, SetImagen

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'content')

class mangaForm(forms.ModelForm):
    class Meta:
        model = Manga3
        fields = ['idManga', 'nombreManga', 'ano_publicacion','tsubida','mangaka','sinopsis','editorial','genero','estado','imagen'] 


class imagenForm(forms.Form):
    idLote = forms.CharField(max_length=255, primary_key= True)
    capitulo = forms.CharField(max_length=255)
    manga = forms.ModelChoiceField(queryset=Manga3.objects.all())       
    grupoImagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))