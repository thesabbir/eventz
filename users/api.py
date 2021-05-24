from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from users.models import UserModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['email', 'first_name', 'last_name']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [path('', include(router.urls))]
