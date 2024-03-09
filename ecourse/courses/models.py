from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):
    pass

class Category(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Courses (BaseModel):
    name = models.CharField(max_length=50)
    desciption = RichTextField()
    image = models.ImageField(upload_to='courses/%Y/%m/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

class Lesson (BaseModel):
    name = models.CharField(max_length=50)
    desciption = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m/', null=True, blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

class Tag (BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name