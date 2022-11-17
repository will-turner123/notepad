from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Note(models.Model):
    content = models.TextField(max_length=4000, blank=True, default="")
    uuid = models.TextField(default=uuid.uuid4().hex[:8], editable=False, max_length=8, unique=True)
    online_users = models.IntegerField(default=0)
    # def get_absolute_url(self):
    #     return reverse('view_note', args=[self.uuid])