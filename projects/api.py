# myapp/api.py
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Project


class ProjectResource(ModelResource):
    class Meta:
        queryset = Project.objects.all()
        # Very insecure
        authorization= Authorization()
