from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from events.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        # fields = ['name',
        #           'event_link',
        #           'description',
        #           'merchandises',
        #           'orders',
        #           'tags',
        #           'user',
        #           'photo',
        #           'age_gate',
        #           'price',
        #           'start_date',
        #           'end_date']


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


router = routers.SimpleRouter()
router.register(r'events', EventViewSet)
urlpatterns = [path('', include(router.urls))]
