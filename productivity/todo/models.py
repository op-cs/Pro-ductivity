from django.db import models

# Create your models here.

class task(models.Model):
    summary = models.CharField('Summary', max_length=500)
    detail = models.TextField('Detail')
    deadline = models.DateTimeField(blank=True)
    
    def __str__(self):
        return self.summary