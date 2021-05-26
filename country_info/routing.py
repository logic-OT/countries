from django.urls import path
from . import consumers
ws_urls = [
    path('realt_search/',consumers.search_consumer.as_asgi())
]