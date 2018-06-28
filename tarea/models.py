from django.db import models
from django.utils import timezone

class Tarea(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    text = models.TextField()
    duration = models.CharField(max_length = 50)
    created_date = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.text
