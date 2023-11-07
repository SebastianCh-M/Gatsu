from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home.html', context)

@method_decorator(login_required, name='dispatch')
class RecientesView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'recientes.html', context)

@method_decorator(login_required, name='dispatch')
class TopMangasView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'TopMangas.html', context)

@method_decorator(login_required, name='dispatch')
class SobreGatsuView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'SobreGatsu.html', context)

class LoginView(View):
        def get(self, request, *args, **kwargs):
            context = {}
            return render(request, 'registration/login.html', context)