from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=500)
    item = models.ForeignKey('items.Item')

    def __unicode__(self):
        return '%i - %s' % (self.id, self.title)
