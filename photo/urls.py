from django.urls import path
from photo import views


app_name = 'photo'
urlpatterns = [

    # ex) /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # ex) /photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # ex) /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # ex) /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),

]




# from django.urls import path
# from django.views.generic import ListView, DetailView

# from photo.models import Album,Photo

# app_name = 'photo'
# urlpatterns = [

    # ex) /photo/
    # path('', ListView.as_view(model=Album), name='index'),

    # ex) /photo/album/, same as /photo/
    # path('', ListView.as_view(model=Album), name='album_list'),

    # ex) /photo/album/99/
    # path('album/<int:pk>/', DetailView.as_view(model=Album), name='album_detail'),

    # ex) /photo/album/99/
    # path('photo/<int:pk>/', DetailView.as_view(model=Photo), name='photo_detail'),

# ]