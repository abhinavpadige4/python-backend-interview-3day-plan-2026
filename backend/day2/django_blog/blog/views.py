"""
Blog views for the django_blog project.
"""

from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Post instances.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer