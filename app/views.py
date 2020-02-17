from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Author, Book
from .serializer import AuthorSerializer, BookSerializer
#from .filters import AuthorFilter, BookFilter

from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    @action(detail=True)
    def book(self, request, pk=None):
        return Response(list(Book.objects.filter(author=pk).values()))

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    @action(detail=True)
    def author(self, request, pk=None):
        return Response(list(Author.objects.filter(book=pk).values()))


# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
#     UpdateAPIView
# )
#
#
# class AuthorListView(ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (permissions.AllowAny, )
#
#
# class AuthorDetailView(RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (permissions.AllowAny, )
#
#
# class AuthorCreateView(CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (permissions.IsAuthenticated, )
#
#
# class AuthorUpdateView(UpdateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (permissions.IsAuthenticated, )
#
#
# class AuthorDeleteView(DestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     # permission_classes = (permissions.IsAuthenticated, )
