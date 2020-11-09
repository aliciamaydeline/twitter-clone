import random
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Tweet(models.Model):
  # foreign key: many users can have many tweets, but one tweet can only have one user
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField(blank=True, null=True)
  image = models.FileField(upload_to="images/", blank=True, null=True)

  # def __str__(self):
  #   return self.content

  class Meta:
    ordering = ['-id']  # descending order

  def serialize(self):
    return {
      "id": self.id,
      "content": self.content,
      "likes": random.randint(0, 200),
    }