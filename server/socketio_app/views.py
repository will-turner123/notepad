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
def connect(sid, environ, auth):
    logger.info("connect ", sid)

    sio.emit("connected", namespace='/socket.io', room=sid)


@sio.on("authenticate", namespace='/socket.io')
def authenticate(sid, environ):
    sio.save_session(sid, {"user": "test"})
    # This will be useful if/when we do authentication. Real time notifications

@sio.on("join-note")
def join(sid, environ):
    logger.info('joining a note!!')
    uuid = environ.get("uuid")
    if uuid:
        note = Note.objects.filter(uuid=uuid).first()
        if note:
            # with sio.session(sid) as session:
                # session["note_id"] = note.uuid
                # session["username"] = None
                # session["room"] = note.uuid
                # sio.enter_room(sid, uuid)
            data = {
                "content": note.content,
                "uuid": note.uuid,
                "online_users": note.online_users+1,
            }
            sio.emit("new-join", data)
            note.online_users += 1
            note.save()
            # sio.emit("ok", {"data": note.content, "count": 0})
        else:
            sio.emit("error", {"data": "Note not found", "count": 0})
    else:
        sio.emit("error", {"data": "Note not found", "count": 0})

@sio.event(namespace='/socket.io')
def disconnect(sid):
    logger.info("disconnect ", sid)
    with sio.session(sid) as session:
        note_id = session.get("note_id")
        if note_id:
            note = Note.objects.filter(uuid=note_id).first()
            if note:
                note.online_users -= 1
                note.save()
                sio.emit("user-disconnected", {"online_users": note.online_users}, namespace='/socket.io')


@sio.on("write-note", namespace='/socket.io')
def write(sid, environ):
    # logger.info('writing a note!!')
    # with sio.session(sid) as session:
    #     note_id = session.get("note_id")
    #     if note_id:
    #         note = Note.objects.filter(uuid=note_id).first()
    #         if note:
    #             note.content = data.get("content")
    #             sio.emit("note-updated", {"content": note.content}, room=note.uuid)
    #             note.save()
    note_id = environ.get("uuid")
    content = environ.get("content")
    if note_id:
        note = Note.objects.filter(uuid=note_id).first()
        if note:
            note.content = content
            # sio.emit("note-updated", {"content": note.content}, room=note.uuid, namespace='/socket.io')
            sio.emit("note-updated", {"content": note.content}, namespace='/socket.io')
            note.save()
    else:
        sio.emit("error", {"data": "Note not found", "count": 0})