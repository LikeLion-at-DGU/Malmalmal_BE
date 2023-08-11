from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import Profile, EditorProfile

class Post(models.Model):
    # id = models.AutoField(primary_key=True, blank=False, null=False, default=0)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    like = models.ManyToManyField(User, related_name='liked_post', blank=True, default=0)
    published_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


class Editor_Post(models.Model):
    # id = models.AutoField(primary_key=True, blank=False, null=False, default=0)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    recruit_date = models.DateField(blank=False, null=False)
    place = models.CharField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=100, blank=False, null=False)
    like = models.ManyToManyField(User, related_name='editor_liked_post', blank=True, default=0)
    scarp = models.ManyToManyField(User, related_name='scarped_post', blank=True, default=0)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title