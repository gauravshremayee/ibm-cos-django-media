from django.db import models


# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255, default='Test')
    file = models.ImageField(upload_to='images', blank=False)

    def __str__(self):
        return self.title
