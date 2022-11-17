# import uuid
# from .models import Note

# def generate_uuid():
#     u = uuid.uuid4().hex
#     u = u[:7]
#     is_unique = Note.objects.filter(uuid=u).first() == None
#     return u if is_unique else generate_uuid()