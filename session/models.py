from django.db import models

class Session(models.Model):
    date = models.DateField(blank=False)
    title = models.TextField(blank=False)



