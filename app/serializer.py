from .models import Author, Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())
    author = serializers.SlugRelatedField(many=True, queryset=Author.objects.all(), slug_field='name')
    class Meta:
        model = Book
        fields = ('id', 'name', 'summary', 'author')

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name')
