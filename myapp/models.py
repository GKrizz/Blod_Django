from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=255)
    Content = models.TextField(null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default=1)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)

