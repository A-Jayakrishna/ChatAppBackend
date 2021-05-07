"""
ASGI config for chatBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

# import os
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter,URLRouter
# from django.core.asgi import get_asgi_application
# import app.routing as route

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatBackend.settings')

# application = ProtocolTypeRouter({
#     "http":get_asgi_application(),
#     "websocket":AuthMiddlewareStack(
#         URLRouter(route.websocket_urlpatterns)
#     ),
# })

import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatBackend.settings')
django.setup()
application = get_default_application()