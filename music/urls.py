from django.urls import path
from music import views

app_name = 'music'

urlpatterns = [
    path('add/album', views.AddAlbum, name='addalbum'),
    path('delete/album/<int:id>', views.DeleteAlbum, name='deletealbum'),
    path('edit/album/<int:id>', views.EditAlbum, name='editalbum'),
]