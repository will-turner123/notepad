from django.db import models
from django.urls import reverse
import os

from .utils import h_encode

# Create your models here.
class Note(models.Model):
    content = models.TextField(max_length=4000, blank=True)

    def __str__(self):
        return f'Note ({len(self.content)} characters long'
    
    def get_hashid(self):
      return h_encode(self.pk)

    def get_absolute_url(self):
        return reverse('notes', args=[self.pk])