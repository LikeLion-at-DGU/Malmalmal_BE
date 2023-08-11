from django.db import models

# Create your models here.

class IntroWriting(models.Model):
    question = models.CharField(max_length=50, blank=False, null=False)
    content = models.TextField(blank=False, null=False)
    def __str__(self):
        return self.question