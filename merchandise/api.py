from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from merchandise.models import Merchandise


class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = '__all__'


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer


router = routers.SimpleRouter()
router.register(r'merchandises', MerchandiseViewSet)
urlpatterns = [path('', include(router.urls))]

