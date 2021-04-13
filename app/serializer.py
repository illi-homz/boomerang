from app import models
from rest_framework import routers, serializers, viewsets


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.New
        fields = '__all__'


class NewViewSet(viewsets.ModelViewSet):
    queryset = models.New.objects.all()
    serializer_class = NewSerializer
