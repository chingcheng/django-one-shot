from django.db import models

# Create your models here.
class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    # This tells Django how to convert our model into a string
    # when we print() it, or when the admin displays it
    def __str__(self):
        return self.name
