from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .authentication import CustomAuthentication
from .models import Book, Author, Member
from .serializers import BookSerializer, AuthorSerializer, MemberSerializer
from .pagination import BookLimitPagination, MemberLimitPagination, AuthorLimitPagination

class BookView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomAuthentication, SessionAuthentication)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookLimitPagination

class AuthorView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomAuthentication, SessionAuthentication)

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = AuthorLimitPagination

class MemberView(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (CustomAuthentication, SessionAuthentication)

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = MemberLimitPagination
