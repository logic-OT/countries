from channels.generic.websocket import WebsocketConsumer
import json
from . import scraper


class search_consumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        self.send(json.dumps({'response':scraper.countries}))

    def receive(self,text_data):
        data = json.loads(text_data)['message']
        results = scraper.search_res(data)
        self.send(json.dumps({'response':results}))
        