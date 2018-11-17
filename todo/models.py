from django.db import models


class ToDoItem(models.Model):
    name = models.CharField(max_length=80)
    is_done = models.BooleanField(default=False)
