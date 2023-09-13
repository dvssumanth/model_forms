from django.db import models
from django.core import validators
from django.forms import ValidationError
def min_len(s):
    if len(s)<4:
        raise ValidationError('len is less')
# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(primary_key=True,max_length=100,validators=[min_len])

    def __str__(self) -> str:
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    renterpassword=models.CharField(max_length=100)