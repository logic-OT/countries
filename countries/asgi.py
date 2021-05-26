"""
ASGI config for countries project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
django_asgi = get_asgi_application() 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'countries.settings')



from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from country_info.routing import ws_urls

application = ProtocolTypeRouter({
    'http': django_asgi,
    'websocket': AuthMiddlewareStack(URLRouter(ws_urls))
})
