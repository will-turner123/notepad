from django.db import models
from django.urls import reverse
import os

# Create your models here.
class Note(models.Model):
    content = models.TextField(max_length=4000, blank=True)

    def __str__(self):
        return f'Note ({len(self.content)} characters long'
    
    def get_absolute_url(self):
        return reverse('notes', kwargs={'pk': self.pk})