from django.shortcuts import render


async_mode = 'eventlet' # TODO: Move to eventlet

import os
from django.http import HttpResponse
import socketio


basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode,
                      cors_allowed_origins='*')
# thread = None

from notes.models import Note

@sio.on('*', namespace='/socket.io')
def all_events(sid, data):
    print('message received with ', data)

@sio.on("test", namespace='/socket.io')
def connect(sid, environ):
    print("connect ", sid)

    sio.save_session(sid, {"sid": sid, "username": None, "note_id": None})
    sio.emit("connected", {"sid": sid}, room=sid)


@sio.on("authenticate", namespace='/socket.io')
def authenticate(sid, environ):
    sio.save_session(sid, {"user": "test"})
    # This will be useful if/when we do authentication. Real time notifications

@sio.on("join-note", namespace='/socket.io')
def join(sid, environ):
    print('joining a note!!')
    uuid = environ.get("uuid")
    if uuid:
        note = Note.objects.filter(uuid=uuid).first()
        if note:
            with sio.session(sid) as session:
                session["note_id"] = note.uuid
                session["username"] = None
                sio.enter_room(sid, uuid)
                data = {
                    "content": note.content,
                    "uuid": note.uuid,
                    "online_users": note.online_users+1,
                }
                sio.emit("new-join", data, room=note.uuid)
                note.online_users += 1
                note.save()
            # sio.emit("ok", {"data": note.content, "count": 0})
        else:
            sio.emit("error", {"data": "Note not found", "count": 0})

@sio.event(namespace='/socket.io')
def disconnect(sid):
    print("disconnect ", sid)
    with sio.session(sid) as session:
        note_id = session.get("note_id")
        if note_id:
            note = Note.objects.filter(uuid=note_id).first()
            if note:
                note.online_users -= 1
                note.save()
                sio.emit("user-disconnected", {"online_users": note.online_users}, room=note.uuid)


@sio.on("write-note", namespace='/socket.io')
def write(sid, data):
    with sio.session(sid) as session:
        note_id = session.get("note_id")
        if note_id:
            note = Note.objects.filter(uuid=note_id).first()
            if note:
                note.content = data
                note.save()
                sio.emit("note-updated", {"content": note.content}, room=note.uuid)