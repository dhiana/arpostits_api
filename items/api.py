from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Item


class ItemResource(ModelResource):
    tasks = fields.ToManyField('tasks.api.TaskResource', 'task_set',  related_name='item', full=True)
    class Meta:
        queryset = Item.objects.all()
        # Very insecure
        authorization = Authorization()
