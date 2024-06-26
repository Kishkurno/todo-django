from django.db import models

from user.models import User

class Todo(models.Model):
    title = models.TextField()
    description = models.TextField()
    isDone = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos',null=True)
    class Meta:
        ordering = ['id']

