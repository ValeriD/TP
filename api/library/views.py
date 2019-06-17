from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Book, Author, Member
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer
from .pagination import BookLimitPagination, MemberLimitPagination, AuthorLimitPagination

class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = BookLimitPagination

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorLimitPagination

class MemberView(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = MemberLimitPagination
