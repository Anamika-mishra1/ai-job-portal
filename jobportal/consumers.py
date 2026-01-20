import json
from channels.generic.websocket import AsyncWebsocketConsumer

class JobConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'jobs'
        await self.channel_layer.group_add(self.room_group_name, self
