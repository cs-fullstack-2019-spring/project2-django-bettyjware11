from django.conf import settings
from django.urls import path
from django.views.static import serve

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('allEntries/', views.allEntries, name="allEntries"),
    path('relatedEntries/', views.relatedEntries, name="relatedEntries"),
    path('createUser/', views.createUser, name="createUser"),
    path('editUser/<int:userID>/', views.editUser, name="editUser"),
    path('addNewEntry/', views.addNewEntry, name="addNewEntry"),
    path('gotEntryInfo/', views.gotEntryInfo, name="gotEntryInfo"),
    path('addRelated/', views.addRelated, name="addRelated"),
    path('yourEntries/', views.yourEntries, name="yourEntries"),
    path('editEntries/<int:wikipostsID>/', views.editEntries, name="editEntries"),
    path('editRelated/<int:relatedID>/', views.editRelated, name="editRelated"),
    path('deleteEntries/<int:wikipostsID>/', views.deleteEntries, name="deleteEntries"),
    path('deleteRelated/<int:relatedID>/', views.deleteRelated, name="deleteRelated"),
    path('searchPosts/<int:wikipostsID>/', views.searchPosts, name="searchPosts"),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]