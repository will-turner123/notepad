from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django.http import JsonResponse
from .models import Note
import json

# Create your views here.
def view_note(request, pk):
    note = Note.objects.get(pk=pk)
    return JsonResponse({'content': note.content})

@csrf_exempt
def save_note(request, pk=None):
    if request.method != "POST":
        return JsonResponse({'error': 'Request is not post type!'}, status=400)
    
    print(request.body)
    data = json.loads(request.body)
    content = data['content']
    
    if pk != None:
        note = Note.objects.filter(pk=pk)
        if not note.exists():
            return JsonResponse({}, status=400)
        note = note.first()
        note.content = content
    else:
        print(123)
        note = Note.objects.create(content=content)
        pk = note.pk
    note.save()
    print(pk)
    
    return JsonResponse({'pk': pk}, status=200)