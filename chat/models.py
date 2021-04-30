from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

        

class Message1(models.Model):
    author1 = models.ForeignKey(User, related_name='author_messages1', on_delete=models.RESTRICT)
    content1 = models.TextField()
    timestamp1 = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author1.username

    def last_10_messages():
        return Message1.objects.order_by('timestamp1').all()[:20]

        