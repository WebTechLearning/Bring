from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name
        
class Transportation(models.Model):
    name = models.CharField(max_length=16)
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    place = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.PositiveSmallIntegerField()
    
    GENDER_CHOICES = (
        ('m', '男'),
        ('f', '女'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    trans = models.ManyToManyField(Transportation)
    items = models.ManyToManyField(Item)
    
    def __unicode__(self):
        return self.place

    def get_duration(self):
        return (self.end_date - self.start_date).days + 1
   
    def save(self, *args, **kwargs):
        self.duration = self.get_duration()
        super(Event, self).save(*args, **kwargs)