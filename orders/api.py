from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)
urlpatterns = [path('', include(router.urls))]
