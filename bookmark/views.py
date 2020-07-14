from django.views.generic import ListView, DeleteView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DeleteView):
    model = Bookmark

