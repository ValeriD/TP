from django.db import models


class Author(models.Model):
    firstName  = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    def __str__(self):
        return self.firstName + " " +self.lastName

class Book(models.Model):
    name  = models.CharField(max_length = 50)
    ISBN = models.CharField(max_length = 20)
    author = models.ForeignKey(Author, null=True)

    def __str__(self):
        return self.name
class Member(models.Model):
    name = models.CharField(max_length = 50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
