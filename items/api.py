from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import Item


class ItemResource(ModelResource):
    class Meta:
        queryset = Item.objects.all()
        # Very insecure
        authorization = Authorization()
