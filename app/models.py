from django.db import models
import uuid

# Create your models here.

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return "%s | %s " % (
            self.name,
            self.id
        )

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    author = models.ManyToManyField(Author, blank=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return " %s | %s |%s" % (
            self.name,
            self.summary,
            self.author
        )
