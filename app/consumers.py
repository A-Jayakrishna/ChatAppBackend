import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import User,Message
import smtplib
from channels.db import database_sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room = self.scope['url_route']['kwargs']['room_name']
        self.group = 'chat_%s' % self.room

        # Join room group
        await self.channel_layer.group_add(
            self.group,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['msg']

        await self.createMsg(self.room,message[0],message[1])

        # Send message to room group
        await self.channel_layer.group_send(
            self.group,
            {
                'type': 'chat_message',
                'msg': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['msg']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'msg': message
        }))

    @database_sync_to_async
    def createMsg(self,convo,sender,msg):
         obj=Message(convo=convo,sender=sender,msg=msg)
         obj.save()
         if(convo!="grp" and msg=="notify"):
             receiver = convo.replace(str(sender)+"_", "")
             obj2=User.objects.get(id=int(receiver))
             obj3=User.objects.get(id=int(sender))
             if(obj2.email=="a.jaiki000@gmail.com"):
                 try:
                     # gmailaddress = "your email "
                     # gmailpassword = "your pass"
                     mailto = obj2.email
                     subject="Notification from Chatapp"
                     body="you have got message from "+obj3.name
                     msg = f'Subject: {subject}\n\n{body}'
                     mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                     mailServer.starttls()
                     mailServer.login(gmailaddress , gmailpassword)
                     mailServer.sendmail(gmailaddress, mailto , msg)
                     print(" \n Sent!")
                     mailServer.quit()
                 except:
                    print("An exception occurred")
