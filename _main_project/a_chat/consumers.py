import json
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer

from .models import ChatRoom, Message


class ChatConsumer(WebsocketConsumer):
	def connect(self):
		self.user = self.scope['user']
		self.room_name = self.scope['url_route']['kwargs']['room_name']
		self.room = get_object_or_404(ChatRoom, room_name=self.room_name)

		async_to_sync(self.channel_layer.group_add)(
			self.room_name,
			self.channel_name,
		)

		self.accept()


	def disconnect(self, close_code):
		async_to_sync(self.channel_layer.group_discard)(
			self.room_name,
			self.channel_name,
		)


	def receive(self, text_data):
		text_data_json = json.loads(text_data)
		msg_content = text_data_json['msg_content']

		message = Message.objects.create(
			room=self.room,
			author=self.user,
			msg_content=msg_content,
		)

		event = {
			'type': 'message_handler',
			'message_id': message.id,
		}

		async_to_sync(self.channel_layer.group_send)(
			self.room_name,
			event
		)


	def message_handler(self, event):
		message_id = event['message_id']
		message = Message.objects.get(id=message_id)

		context = {
			'message': message,
			'user': self.user,
		}
		html = render_to_string('a_chat/partials/chat_message_p.html', context=context)
		self.send(text_data=html)


