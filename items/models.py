from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=500)
    project = models.ForeignKey('projects.Project')
    
    def __unicode__(self):
        return '%i - %s' % (self.id, self.title)
