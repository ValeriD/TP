from django.shortcuts import render
from rest_framework import viewsets
from .models import Book, Author, Member
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer
from .pagination import BookLimitPagination

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookLimitPagination

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
