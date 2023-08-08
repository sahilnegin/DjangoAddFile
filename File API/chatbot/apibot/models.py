# apibot/models.py

from django.db import models

class Chatbot(models.Model):
    files = models.FileField(upload_to="chatbot_files/", blank=True)

    def __str__(self):
        return f"Chatbot {self.id}"
