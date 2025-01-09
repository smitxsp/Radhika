from django.db import models
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    desc = models.TextField()
    timeStamp = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return 'massage from' + self.name + '-' + self.email