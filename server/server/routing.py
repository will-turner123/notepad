# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.conf.urls import url
# from channels.security.websocket import AllowedHostsOriginValidator
# from notes.consumers import NoteConsumer

# application = ProtocolTypeRouter({
#   'websocket': AllowedHostsOriginValidator(
#     URLRouter(
#       [
#         url("", NoteConsumer)
#       ]
#     )
#   )
# })