from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from .models import Note

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note # A que modelo se corresponde
        fields = '__all__' # Campos a serializar