from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import logout

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'home.html', context)


class RecientesView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'recientes.html', context)


class TopMangasView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'TopMangas.html', context)


class SobreGatsuView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'SobreGatsu.html', context)

class LoginView(View):
        def get(self, request, *args, **kwargs):
            context = {}
            return render(request, 'registration/login.html', context)