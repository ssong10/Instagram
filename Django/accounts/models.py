from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        processors = [ResizeToFill(100 * 100)],
        format = 'JPEG',
        options = {'quality': 80}
    )