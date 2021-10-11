from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated']

    def __str__(self):
        return self.title
    

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='_media/posts/default_image.png', upload_to='posts/%Y/%m/%d', blank=True, null=True)
