from django.db import models

class NotePad(models.Model):

    title = models.CharField(max_length=100)
    body = models.TextField()
