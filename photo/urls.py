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

# --- /photo/album/ (add, change, update, delete)
    # ex) /photo/album/add/
    path('album/add/', views.AlbumPhotoCV.as_view(), name='album_add'),

    # ex) /photo/album/change/
    path('album/change/', views.AlbumChangeLV.as_view(), name='album_change'),

    # ex) /photo/album/99/update/
    path('album/<int:pk>/update/', views.AlbumPhotoUV.as_view(), name='album_update'),

    # ex) /photo/album/99/delete/
    path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'),

# --- /photo/photo/ (add, change, update, delete)
    # ex) /photo/photo/add/
    path('photo/add/', views.PhotoCV.as_view(), name='photo_add'),

    # ex) /photo/photo/change/
    path('photo/change/', views.PhotoChangeLV.as_view(), name='photo_change'),

    # ex) /photo/photo/99/update/
    path('photo/<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'),

    # ex) /photo/photo/99/delete/
    path('photo/<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'),

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