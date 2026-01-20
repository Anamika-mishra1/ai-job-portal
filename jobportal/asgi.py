import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import jobportal.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            jobportal.routing.websocket_urlpatterns
        )
    ),
})
