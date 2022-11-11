from django.http import JsonResponse
from .models import Note

# Create your views here.
def view_note(request, pk):
    note = Note.objects.get(pk=pk)
    return JsonResponse({'content': note.content})

def save_note(request, pk):
    content = request.POST.get('content')
    if pk != None:
        note = Note.objects.get(pk=pk)
        if not note.exists():
            return JsonResponse({'status': 400})
        note.content = content
    else:
        note = Note.objects.create(content=content)
    return JsonResponse({'success': 'yassss'})