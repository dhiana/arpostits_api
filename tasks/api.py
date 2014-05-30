from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Task


class TaskResource(ModelResource):
    class Meta:
        queryset = Task.objects.all()
        # Very insecure
        authorization = Authorization()
