from django.shortcuts import render
from django.views.generic import View
from .forms import PostCreateForm

# Create your views here.

class MangaListView(View):
    def get(self, request, *args, **kwargs):
        context={
            
        }
        return render(request, 'manga_list.html', context )
    
class MangaCreateView(View):
    def get(self, request,*args, **kwargs):
        context={
            
        }
        return render(request, 'manga_create.html', context)
    
    def post(self, request,*args, **kwargs):
        context={
            
        }
        return render(request, 'manga_create.html', context)