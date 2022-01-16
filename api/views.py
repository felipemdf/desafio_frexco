from rest_framework import viewsets, generics
from api.models import Region, Fruit
from api.serializer import RegionSerializer, FruitSerializer, ListFruitsPerRegion

class RegionsViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class ListFruitsPerRegion(generics.ListAPIView):
    def get_queryset(self):
        queryset = Fruit.objects.filter(region_id = self.kwargs['pk'])
        return queryset
    
    serializer_class = ListFruitsPerRegion
