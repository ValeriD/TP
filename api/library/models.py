from django.db import models


class Book(models.Model):
    name  = models.CharField(max_length = 50)
    ISBN = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
