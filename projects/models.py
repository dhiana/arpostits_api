from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=500)
    def __unicode__(self):
        return '%i - %s' % (self.id, self.title)
