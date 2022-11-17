# import asyncio
# import json
# from channels.consumer import AsyncConsumer
# from .models import Note

  

# class NoteConsumer(AsyncConsumer):

#   # Dispatching
#   async def websocket_connect(self, event):
    
#     self.note_id = event.get('uuid')
#     # TODO: Handle if doesn't exist
#     if self.note_id:
#       self.note = Note.objects.filter(uuid=self.note_id).first()
#       await self.send({
#         'type': 'websocket.accept',
#         'content': self.note.content,
#       })
#     else:
#       await self.send({
#         'type': 'websocket.accept'
#       })

#   async def websocket_receive(self, event):
#     note_content = event.get('content', None)

#     await self.channel_layer.group_send(
#       self.note_id,
#       {
#         "type": "board_message",
#         "text": note_content
#       })
#     self.note.content = note_content
#     self.note.save()

#   async def websocket_disconnect(self, event):
#     print('disconnected', event)
