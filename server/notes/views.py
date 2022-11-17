from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from django.http import JsonResponse
import json
# import uuid
from .models import Note


# Create your views here.
@csrf_exempt
def view_note(request, note_id):
    # TODO: 404 if note doesn't exist
    note = Note.objects.filter(uuid=note_id).first()
    return JsonResponse({'content': note.content, 'uuid': note.uuid})

@csrf_exempt
def create_note(request):
    if request.user:
        # TODO: give it an owner
        pass

    note = Note.objects.create()
    # TODO: better way to jsonify this
    response = {
        'uuid': note.uuid,
        'content': note.content
    }

    return JsonResponse(response)

# @csrf_exempt
# def save_note(request, pk=None):
#     if request.method != "POST":
#         return JsonResponse({'error': 'Request is not post type!'}, status=400)
    
#     data = json.loads(request.body)
#     content = data['content']
    
#     if pk != None:
#         note = Note.objects.filter(pk=pk)
#         if not note.exists():
#             return JsonResponse({}, status=400)
#         note = note.first()
#         note.content = content
#     else:
#         note = Note.objects.create(content=content)
#         pk = note.pk
#     note.save()
    
#     hash = note.get_hashid()
#     print(hash)
#     return JsonResponse({'hash': hash}, status=200)