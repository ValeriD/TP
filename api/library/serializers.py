from rest_framework import serializers
from .models import Book, Author, Member

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id','url', 'name', 'ISBN', 'author')

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'url', 'firstName', 'lastName')

class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'url', 'name', 'books')
