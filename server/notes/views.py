from django.http import JsonResponse
from .models import Note

# Create your views here.
def view_note(request, pk):
    note = Note.objects.get(pk=pk)
    print(note.content)
    return JsonResponse({'content': note.content})