from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
