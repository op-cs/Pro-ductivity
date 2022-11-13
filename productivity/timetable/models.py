from django.db import models

class Days(models.Model):
    Day = models.CharField(max_length=200)
    def __str__(self):
        return self.Day
class time_task(models.Model):
    Day = models.ForeignKey(Days, on_delete=models.CASCADE)
    Time = models.TimeField()
    Title = models.CharField('Title', max_length=300)
    Description = models.TextField('Description')
    
    def __str__(self):
        return self.Title

# Create your models here.
