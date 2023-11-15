from django.shortcuts import render, redirect
from django.views.generic import View
from .models import tipoEstado, tipoSubida, Manga3, Imagen
from django.core.exceptions import ObjectDoesNotExist
import uuid



