from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class AbstractNotesModel(models.Model):

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NotesUser(AbstractNotesModel, AbstractUser):

    phone_number = models.CharField()


class Note(AbstractNotesModel):

    title = models.CharField(max_length=80)
    description = models.TextField()

    created_by = models.ForeignKey(to=NotesUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
