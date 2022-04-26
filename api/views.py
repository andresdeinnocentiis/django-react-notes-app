from msilib.schema import ServiceInstall
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializers import NoteSerializer

#from django.http import JsonResponse #Una vez instalado djangorestframework esto ya no hace falta

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    
    return Response(routes)
    #return JsonResponse(routes, safe=False) # "safe" significa que vamos a poder retornar mas data que solo un diccionario
    
    
@api_view(['GET'])
def getNotes(request):    
    notes = Note.objects.all().order_by('-updated') # Esto es un queryset
    serializer = NoteSerializer(notes, many=True) # many=True: indica que vamos a pasar multiples objetos (sino pasa un unico objeto)
    return Response(serializer.data) # Como no se puede devolver un objeto en la web, hay que serializarlo, y pasar la data del serializador
   
    
@api_view(['GET'])
def getNote(request, primary_key):    
    notes = Note.objects.get(id=primary_key) # Esto es un queryset
    serializer = NoteSerializer(notes, many=False) # many=False: indica que vamos a pasar un unico objeto
    return Response(serializer.data) # Como no se puede devolver un objeto en la web, hay que serializarlo, y pasar la data del serializador


@api_view(['POST'])
def createNote(request):    
    data = request.data
    note = Note.objects.create(
        body=data['body']    
    )
    serializer = NoteSerializer(note, many=False)
    
    return Response(serializer.data)

    
@api_view(['PUT'])
def updateNote(request, primary_key):    
    data = request.data
    note = Note.objects.get(id=primary_key)
    serializer = NoteSerializer(instance=note, data=data)
    
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data) # Como no se puede devolver un objeto en la web, hay que serializarlo, y pasar la data del serializador
    
    
@api_view(['DELETE'])
def deleteNote(request, primary_key):    
    note = Note.objects.get(id=primary_key)
    note.delete()
    return Response('Note was deleted') # Como no se puede devolver un objeto en la web, hay que serializarlo, y pasar la data del serializador


