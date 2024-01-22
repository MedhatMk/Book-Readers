from email.policy import default
from enum import unique
from random import choices
from turtle import mode
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model
from pyuploadcare.dj.models import ImageField
from pyuploadcare import File, Uploadcare
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=150)
    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=255, unique=True, blank=False)
    cover = models.ImageField(upload_to='media',blank=True, null=True)
    pages = models.IntegerField(blank=False, null = False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(blank=False)
    author = models.ForeignKey(get_user_model(),on_delete=models.SET_NULL,null=True,related_name='authored_books')
    created_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, related_name='created_books')
    average_rate = models.FloatField(default = 0)

    # def calculate_rate_avg(self):


    def __str__(self):
        return self.title

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1 star'),
        (2, '2 stars'),
        (3, '3 stars'),
        (4, '4 stars'),
        (5, '5 stars'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    rate = models.SmallIntegerField(choices=RATING_CHOICES)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)

    # def save(self, *args, **kwargs):
    #     if self.cover and isinstance(self.cover, SimpleUploadedFile):
    #         uploadcare = Uploadcare(public_key='65dacfed96aaa23c8328', secret_key='bdb4a6e1c6641dd290c2')
    #         uploader = uploadcare.simple_uploader
    #         with open(self.cover.name, 'rb') as file_object:
    #             ucare_file = uploader.upload(file_object)
    #         self.cover = ucare_file.uuid
    #     super().save(*args, **kwargs)
