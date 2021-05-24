from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from tags.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# ViewSets define the view behavior.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


router = routers.SimpleRouter()
router.register(r'tags', TagViewSet)
urlpatterns = [path('', include(router.urls))]
