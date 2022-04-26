from django.urls import path
from . import views

urlpatterns = [
    path('routes/', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('notes/create', views.createNote, name="create-note"),
    path('notes/<str:primary_key>/update', views.updateNote, name="update-note"),
    path('notes/<str:primary_key>/delete', views.deleteNote, name="delete-note"),
    
    path('notes/<str:primary_key>/', views.getNote, name="note"),
]