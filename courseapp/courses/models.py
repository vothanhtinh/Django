from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass


class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    description = RichTextField()
    create_day = models.DateTimeField(auto_now_add=True)
    updated_day = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Course(BaseModel):
    subject = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category , on_delete=models.PROTECT)
    image = models.ImageField(upload_to="courses/%Y/%m",null=True)
    def __str__(self):
        return self.subject

# Create your models here.
