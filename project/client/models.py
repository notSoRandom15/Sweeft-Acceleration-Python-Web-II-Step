from django.db import models
from django.utils import timezone

class URL(models.Model):
    short_name = models.CharField(max_length=10, unique=True)
    long_url = models.URLField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return self.short_name
    
