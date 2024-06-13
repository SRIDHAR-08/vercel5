from django.db import models

class class_model(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name