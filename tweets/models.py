import random
from django.db import models

class Tweet(models.Model):
  content = models.TextField(blank=True, null=True)
  image = models.FileField(upload_to="images/", blank=True, null=True)

  def serialize(self):
    return {
      "id": self.id,
      "content": self.content,
      "likes": random.randint(0, 200),
    }