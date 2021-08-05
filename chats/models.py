from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import CharField
# Create your models here.

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_messgaes')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.author.username

    def last_20_messages(room_name):
        messages_of_chat_id = Message.objects.filter(room_name=room_name)
        return messages_of_chat_id.order_by('timestamp').all()[:20]

