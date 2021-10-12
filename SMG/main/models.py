from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from solo.models import SingletonModel


# Create your models here.

class Blog(models.Model):
    image1 = models.ImageField(upload_to='blogs')
    image2 = models.ImageField(upload_to='blogs')
    title = models.CharField(max_length=80, primary_key=True)
    writer = models.CharField(max_length=100)
    short_desc = models.CharField(max_length=80)
    date = models.DateField(blank=False)
    p1 = models.TextField(blank=True, default='')
    p2 = models.TextField(blank=True, default='')
    p3 = models.TextField(blank=True, default='')
    p4 = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['-date']


class StoneType(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='category_image')
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']


class Stone(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='stone_image')
    image2 = models.ImageField(upload_to='stone_image')
    desc = models.TextField(blank=True, default='')
    category = models.ForeignKey(StoneType, on_delete=models.CASCADE)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

class CarouselCategory(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']


class CarouselImages(models.Model):
    image = models.ImageField(upload_to='gallery_image')
    category = models.ForeignKey(CarouselCategory, on_delete=models.CASCADE)
    ordering = models.IntegerField(blank=False, default=1, validators=[MinValueValidator(1)] , primary_key=True)

    class Meta:
        ordering = ['ordering']



# class Chapter(models.Model):
#     chapter_name = models.CharField(max_length=100, primary_key=True)
#     chapter_image = models.ImageField(upload_to='chapter_image')
#     sig = models.BooleanField(default=False)
#     description = models.TextField(blank=True, default='')
#     banner = models.ImageField(blank=True, upload_to='chapter_image')
#     feature1 = models.CharField(max_length=40)
#     feature2 = models.CharField(max_length=40)
#     feature3 = models.CharField(max_length=40)
#     feature1_desc = models.TextField(blank=True, default='')
#     feature2_desc = models.TextField(blank=True, default='')
#     feature3_desc = models.TextField(blank=True, default='')
#     link = models.CharField(max_length=200)
#     haveInitiative = models.BooleanField(default=False)
#     initiative = models.CharField(max_length=500, blank=True, default='')
#     height = models.IntegerField(blank=True, default=100)
#     width = models.IntegerField(blank=True, default=100)
#     ordering = models.IntegerField(default=0)

#     class Meta:
#         ordering = ['ordering']


# class Member(models.Model):
#     id = models.CharField(max_length=100, primary_key=True)
#     chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
#     memberNo = models.IntegerField(blank=False, default=1, validators=[MinValueValidator(1)])
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='photographs')
#     profile = models.CharField(max_length=200, blank=True, default='')

#     class Meta:
#         ordering = ['memberNo']


# class Event(models.Model):
#     date_month = models.CharField(max_length=20)
#     year=models.IntegerField()
#     title = models.CharField(max_length=100, primary_key=True)
#     description = models.TextField()
#     isAward = models.BooleanField(default=False)
#     date= models.DateField(blank=False)

#     class Meta:
#         ordering = ['-date']

