from django.db import models
from django.core.validators import MaxValueValidator

class Item(models.Model):
    title = models.CharField(max_length=500)
    project = models.ForeignKey('projects.Project')
    progress = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    ready = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
    
    def __unicode__(self):
        return '%i - %s' % (self.id, self.title)

    class Meta:
        ordering = ['id']
