from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from users.models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        # fields = ['email', 'first_name', 'last_name', 'country', 'address', 'postal_code', 'mobile', 'date_of_birth',
        #           'gender', 'is_performer', 'is_staff', 'is_active', 'date_joined']
        fields = '__all__'


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
urlpatterns = [path('', include(router.urls))]
