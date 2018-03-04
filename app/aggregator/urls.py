from django.urls import path, include

from rest_framework import routers
from aggregator.views import UserViewSet, QiitaEntryViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'qiitaentries', QiitaEntryViewSet)

urlpatterns = [
    path('', include(router.urls))
]