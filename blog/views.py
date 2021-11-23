
from django.shortcuts import render
# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Blog
from .serializers import BlogSterilizer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


class BlogsList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSterilizer

class BlogDetail(RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Blog.objects.all()
    serializer_class = BlogSterilizer