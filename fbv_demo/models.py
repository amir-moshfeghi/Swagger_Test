from django.db import models

# Create your models here.
from django.db import models

class Medical(models.Model):
    name = models.CharField(max_length=22)
    bloodgroup = models.CharField(max_length=22)
    birthmark = models.CharField(max_length=44)