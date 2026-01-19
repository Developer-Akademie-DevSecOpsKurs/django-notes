from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class AbstractNotesModel(models.Model):

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NotesUser(AbstractNotesModel, AbstractUser):

    phone_number = models.CharField()


class Notes(AbstractNotesModel):

    title = models.CharField(max_length=80)
    description = models.TextField()

    created_by = models.ForeignKey(
        to=NotesUser,
        on_delete=models.CASCADE
    )
