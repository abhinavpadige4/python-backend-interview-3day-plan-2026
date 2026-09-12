"""
Blog models for the django_blog project.
"""

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title

    def summary(self):
        """Return first 100 characters of content."""
        return self.content[:100] + "..." if len(self.content) > 100 else self.content