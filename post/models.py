from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField(max_length=1024)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1)
    published_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='image', blank=True, null=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('details', args=int[self.id])

