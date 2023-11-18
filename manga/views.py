from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DeleteView
from .forms import revistaForm, m_revistaForm, nomMangaForm, m_nomMangaForm, mangaGatsuForm, m_mangaGatsuForm, capituloForm, m_CapituloForm, imagenForm
from .models import tipoEstado, tipoSubida, Revista, NombreManga, MangaGatsu, Capitulo, Imagen
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy


# Create your views here.

class MangaListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'manga_list.html', context )
    
#Metodo POST REVISTA
def formRevista(request):
    if request.method == 'POST':
        form = revistaForm(request.POST)
        if form.is_valid():
            # Si el formulario es valido, se guardan los datos en la tabla
            form.save()
            return redirect('/listaRevista')
    else:
        form = revistaForm()

    return render(request, 'formRevista.html',{'form': form})    

#METODO GET REVISTA
def listaRevista(request):  
    editoriales = Revista.objects.all()
    datos ={'editoriales': editoriales}
    return render(request, 'listaRevista.html', datos)  

#Metodo DELETE REVISTA    
def deleR(request, id):
    dele = Revista.objects.get(id=id)
    dele.delete()
    return redirect('/listaRevista')   

#METODO UPDATE REVISTA 
def updaR(request, id):
    data = Revista.objects.get(id=id)
    form = m_revistaForm(instance=data)

    if request.method == 'POST':
        form = m_revistaForm(request.POST, instance= data)
        if form.is_valid():
            form.save()
        return redirect('/listaRevista')    

    context = {'form': form}
    return render(request, 'modRevista.html', context)  


#Metodo POST nombreManga
def formNombreManga(request):
    if request.method == 'POST':
        form = nomMangaForm(request.POST)
        if form.is_valid():
            # Si el formulario es valido, se guardan los datos en la tabla
            form.save()
            return redirect('/listaNombreManga')
    else:
        form = nomMangaForm()

    return render(request, 'formNombreManga.html',{'form': form})

#METODO GET nombreManga
def listaNombreManga(request):  
    nombres = NombreManga.objects.all()
    datos ={'nombres': nombres}
    return render(request, 'listaNombreManga.html', datos)


#Metodo DELETE nombreManga    
def deleN(request, id):
    dele = NombreManga.objects.get(id=id)
    dele.delete()
    return redirect('/listaNombreManga')   

#METODO UPDATE nombreManga 
def updaN(request, id):
    data = NombreManga.objects.get(id=id)
    form = m_nomMangaForm(instance=data)

    if request.method == 'POST':
        form = m_nomMangaForm(request.POST, instance= data)
        if form.is_valid():
            form.save()
        return redirect('/listaNombreManga')    

    context = {'form': form}
    return render(request, 'modNombreManga.html', context)



#Metodo POST MangaGatsu
def formMangaGatsu(request):
    if request.method == 'POST':
        form = mangaGatsuForm(request.POST, request.FILES)
        if form.is_valid():
            # Si el formulario es valido, se guardan los datos en la tabla
            form.save()
            return redirect('/listaMangaGatsu')
    else:
        form = mangaGatsuForm()

    return render(request, 'formMangaGatsu.html',{'form': form})

#METODO GET MangaGatsu
def listaMangaGatsu(request):  
    mangas = MangaGatsu.objects.all()
    datos ={'mangas': mangas}
    return render(request, 'listaMangaGatsu.html', datos)



#Metodo DELETE nombreManga    
def deleM(request, id):
    dele = MangaGatsu.objects.get(id=id)
    dele.delete()
    return redirect('/listaMangaGatsu')   

#METODO UPDATE nombreManga 
def updaM(request, id):
    data = MangaGatsu.objects.get(id=id)
    form = m_mangaGatsuForm(instance=data)

    if request.method == 'POST':
        form = m_mangaGatsuForm(request.POST, request.FILES ,instance= data)
        if form.is_valid():
            form.save()
        return redirect('/listaMangaGatsu')    

    context = {'form': form}
    return render(request, 'modNombreManga.html', context)



#Metodo POST Capitulo
def formCapitulo(request):
    if request.method == 'POST':
        form = capituloForm(request.POST)
        if form.is_valid():
            # Si el formulario es valido, se guardan los datos en la tabla
            form.save()
            return redirect('/listaCapitulo')
    else:
        form = capituloForm()

    return render(request, 'formCapitulo.html',{'form': form})


#METODO GET Capitulo
def listaCapitulo(request):  
    capitulos = Capitulo.objects.all()
    datos ={'capitulos': capitulos}
    return render(request, 'listaCapitulo.html', datos)

#Metodo DELETE Capitulo    
def deleC(request, id):
    dele = Capitulo.objects.get(id=id)
    dele.delete()
    return redirect('/listaCapitulo')   

#METODO UPDATE Capitulo 
def updaC(request, id):
    data = Capitulo.objects.get(id=id)
    form = m_CapituloForm(instance=data)

    if request.method == 'POST':
        form = m_CapituloForm(request.POST, instance= data)
        if form.is_valid():
            form.save()
        return redirect('/listaCapitulo')    

    context = {'form': form}
    return render(request, 'modCapitulo.html', context)


#Metodo POST Imagen
def formImagen(request):
    if request.method == 'POST':
        v_imagen = request.FILES.getlist('imagen')
        v_capitulo = request.POST.get('capitulo')  
        capitulo = Capitulo.objects.get(id=v_capitulo)

        for imagen in v_imagen:
            nuevo = Imagen(imagen = imagen)
            nuevo.capitulo = capitulo

            nuevo.save(nuevo)
        

        return redirect('/listaImagen')
    else:
        # Render the form page
        capitulos = Capitulo.objects.all()
        return render(request, 'formImagen.html', {'capitulos': capitulos})
    

#Metodo GET Imagen
def listaImagen(request):  
    imagenes = Imagen.objects.all()
    datos ={'imagenes': imagenes}
    return render(request, 'listaImagen.html', datos)


#Metodo DELETE Imagen    
def deleI(request, id):
    dele = Imagen.objects.get(id=id)
    dele.delete()
    return redirect('/listaImagen')   

#METODO UPDATE Imagen 
def updaI(request, id):
    data = Imagen.objects.get(id=id)
    form = imagenForm(instance=data)

    if request.method == 'POST':
        form = imagenForm(request.POST, request.FILES ,instance= data)
        if form.is_valid():
            form.save()
        return redirect('/listaImagen')    

    context = {'form': form}
    return render(request, 'modImagen.html', context)



#METODO ver capitulo
def verCapitulo(request, id):
    capitulo = Capitulo.objects.get(id=id)
    imagenes = Imagen.objects.all()
    
    return render(request, 'verCapitulo.html', {'capitulos': capitulo, 'imagenes': imagenes})

    
             
    
#class MangaCreateView(View):
#    def get(self, request,*args, **kwargs):
#        context={
#            
#        }
#        return render(request, 'manga_create.html', context)
#    
#    def post(self, request,*args, **kwargs):
#        context={
            
#        }
#        return render(request, 'manga_create.html', context)
    
def formManga(request):
    tEstado=tipoEstado.objects.all()
    tSubida=tipoSubida.objects.all()
    datos = {'tipoEstados':tEstado,'tipoSubidas': tSubida}

    return render(request, 'registrarM.html', datos)


#def guardarManga(request):
    v_idManga=request.POST.get('idManga')
    v_nombreM=request.POST.get('nombreManga')
    v_anoP=request.POST.get('ano_publicacion')
    v_subida=request.POST.get('tsubida')
    v_mangaka=request.POST.get('mangaka')
    v_sinopsis=request.POST.get('sinopsis')
    v_editorial=request.POST.get('editorial')
    v_genero=request.POST.get('genero')
    v_estado=request.POST.get('estado')


    tEstados=tipoEstado.objects.get(estado=v_estado)
    tSubidas=tipoSubida.objects.get(subida=v_subida)

    nuevo=Manga2()
    nuevo.idManga=v_idManga
    nuevo.nombreManga=v_nombreM
    nuevo.ano_publicacion=v_anoP
    nuevo.tsubida=tSubidas
    nuevo.mangaka=v_mangaka
    nuevo.sinopsis=v_sinopsis
    nuevo.editorial=v_editorial
    nuevo.genero=v_genero
    nuevo.estado=tEstados
    

    Manga2.save(nuevo)

    return render(request, 'loginC.html')    




#Formulario de Registro de Mnaga
#def registrarManga(request):
#    if request.method == 'POST':
#        form = mangaForm(request.POST, request.FILES)
#        if form.is_valid():
#            form.save()
#            return redirect('manga_list')
#    else:
#        form = mangaForm()
#    return render(request, 'manga_create.html', {'form': form})

#def manga_list(request):
#    Man = Manga3.objects.all()
#    return render(request, 'manga_list.html', {'mangas': Man})

# Formulario de Registro de Multiples Imagenes




#def registrarImagenes(request):
#    if request.method == 'POST':
#        v_idLote = request.POST.get('idLote')
#        v_capitulo = request.POST.get('capitulo')
#        v_manga = request.POST.get('manga')  # Assuming test is a dropdown or input field in the form
#        v_grupoImagen = request.FILES.getlist('grupoImagen')

#        manga = Manga3.objects.get(manga=v_manga)

        # Create the model instance and save it
#        nuevo=SetImagen()
#        nuevo.idLote=v_idLote
#        nuevo.capitulo=v_capitulo
#        nuevo.manga=manga
#        nuevo.grupoImagen=v_grupoImagen

#        SetImagen.save(nuevo)
        

#        return redirect('manga_list')
#    else:
        # Render the form page
#        mangas = Manga3.objects.all()
#        return render(request, 'capitulos_form.html', {'mangas': mangas})

