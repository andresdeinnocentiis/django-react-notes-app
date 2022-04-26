from django.db import models

# Create your models here.

class Note(models.Model):
    body = models.TextField(null=True, blank=True)
    updated =  models.DateTimeField(auto_now=True) #"auto_now" guarda la fecha cada vez que se actualice
    created = models.DateTimeField(auto_now_add=True) # "auto_now_add" solo guarda la fecha de creacion
    
    def __str__(self):
        return self.body[0:50] # Para que solo se vean los 1eros 50 caracteres xq algunas notas pueden ser muy largas, así se ve mas prolijo

