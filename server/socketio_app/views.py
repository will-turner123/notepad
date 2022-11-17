from django.shortcuts import render


async_mode = 'eventlet' # TODO: Move to eventlet

import os
from django.http import HttpResponse
import socketio
import logging
logger = logging.getLogger(__name__)

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode,
                      cors_allowed_origins='*',
                      logger=True,
                      engineio_logger=True)
# thread = None

from notes.models import Note


@sio.event(namespace='/socket.io')
def connect(sid, environ):

    sio.save_session(sid, {'room': None}, namespace='/socket.io')
    sio.emit("connected", {"data": "connected"}, room=sid, namespace='/socket.io')


@sio.on("authenticate", namespace='/socket.io')
def authenticate(sid, environ):
    sio.save_session(sid, {"user": "test"})
    # This will be useful if/when we do authentication. Real time notifications

@sio.on("join-note", namespace='/socket.io')
def join(sid, uuid):
    logger.info('joining a note!!')
    uuid = str(uuid)
    if uuid:
        note = Note.objects.filter(uuid=uuid).first()
        if note:
            sio.enter_room(sid, uuid, namespace='/socket.io')
            
            with sio.session(sid, namespace='/socket.io') as session:
                if session['room'] not in [uuid, None]:
                    sio.leave_room(sid, session['room'], namespace='/socket.io')
                    sio.emit('left-room', room=session['room'], namespace='/socket.io')
                    previous_room = Note.objects.filter(uuid=session['room']).first()
                    previous_room.online_users -= 1
                    previous_room.save()

                session['room'] = uuid
            data = {
                "content": note.content,
                "uuid": note.uuid,
                "online_users": note.online_users+1,
            }
            sio.emit("new-join", data, namespace='/socket.io', room=uuid)
            note.online_users += 1
            note.save()
        else:
            sio.emit("error", {"data": "Note not found", "count": 0}, namespace='/socket.io', room=sid)
    else:
        sio.emit("error", {"data": "UUID not provided", "count": 0}, namespace='/socket.io', room=sid)

@sio.event(namespace='/socket.io')
def disconnect(sid):
    logger.info("disconnect ", sid)
    with sio.session(sid, namespace='/socket.io') as session:
        note_id = session.get("note_id")
        if note_id:
            note = Note.objects.filter(uuid=note_id).first()
            if note:
                note.online_users -= 1
                sio.emit("user-disconnected", {"online_users": note.online_users}, namespace='/socket.io')
                note.save()


@sio.on("write-note", namespace='/socket.io')
def write(sid, environ):
    note_id = environ.get("uuid")
    content = environ.get("content")
    if note_id:
        note = Note.objects.filter(uuid=note_id).first()
        if note:
            note.content = content
            sio.emit("note-updated", {"content": note.content}, namespace='/socket.io', room=note_id, skip_sid=sid)
            note.save()
    else:
        sio.emit("error", {"data": "Note not found", "count": 0})