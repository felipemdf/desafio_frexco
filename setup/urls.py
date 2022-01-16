from django.contrib import admin
from django.urls import path, include
from api.views import RegionsViewSet,FruitViewSet, ListFruitsPerRegion
from rest_framework import routers

router = routers.DefaultRouter()

router.register('regions', RegionsViewSet, basename='Regions')
router.register('fruits', FruitViewSet, basename='Fruits')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('region/<int:pk>/fruits', ListFruitsPerRegion.as_view()),
]
