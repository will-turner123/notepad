from django.http import JsonResponse
from .models import Note

# Create your views here.
def view_note(request, pk):
    note = Note.objects.get(pk=pk)
    return JsonResponse({'content': note.content})