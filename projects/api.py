from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Project


class ProjectResource(ModelResource):
    items = fields.ToManyField('items.api.ItemResource', 'item_set',  related_name='project', full=True)

    class Meta:
        queryset = Project.objects.all()
        # Very insecure
        authorization= Authorization()
