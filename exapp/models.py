from django.db import models
from django.urls import reverse
from  easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255,verbose_name="Название курса")
    #img = models.ImageField(blank=True,null=True)
    img = ThumbnailerImageField(blank=True,null=True)
    text = models.TextField(verbose_name="Описание курса")
    number = models.IntegerField(blank=True,default=1,verbose_name="Номер по порядку")

    def __str__(self):
        return self.name

    def get_exersuse_count(self):
        return self.exersise_set.all().count()
    def get_absolute_url(self):
        return reverse('course-detail',args=[self.id])

    def get_update_url(self):
        return reverse('course-update',args=[self.id])

class Exersise(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,verbose_name="Название упражнениея")
    text = models.TextField()

    def __str__(self):
        return self.name
