"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import socketio
from django.core.wsgi import get_wsgi_application

from socketio_app.views import sio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

django_app = get_wsgi_application()
application = socketio.WSGIApp(sio, django_app)
import eventlet
eventlet.wsgi.server(eventlet.listen(('', 8000)), application)