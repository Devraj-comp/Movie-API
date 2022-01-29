from rest_framework.serializers import ModelSerializer 
from .models import Genre, Movie


# GENRE SERIALIZER
class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',]

# MOVIE SERIALIZER
class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

