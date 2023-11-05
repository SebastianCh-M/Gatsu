from django.urls import path
from .views import MangaListView, MangaCreateView

app_name="manga"

urlpatterns = [
    path('', MangaListView.as_view(), name="home"),
    path('create/', MangaCreateView.as_view(), name="create"),
]
