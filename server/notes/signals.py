# from django.db.models.signals import post_save
# from django.dispatch import receiver
# import uuid
# from .models import Note

# # def generate_uuid():
# #     u = uuid.uuid4().hex
# #     u = u[:7]
# #     is_unique = Note.objects.filter(uuid=u).first() == None
# #     return u if is_unique else generate_uuid()

# @receiver(post_save, sender=Note)
# def set_uuid(sender, instance, created, **kwargs):
#     if created:
#         instance.uuid = generate_uuid()
#         instance.save()