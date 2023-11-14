from django.db import models
from django.utils import timezone
from school_profile.models import schoolProfile

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(schoolProfile,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    donate_amount = models.IntegerField()
    current_amount = models.IntegerField(blank=True)

    def __str__(self):
        return self.title
    
