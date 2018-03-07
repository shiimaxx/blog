from django.urls import path, include

from rest_framework_nested import routers
from aggregator.views import UserViewSet, QiitaEntryViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'qiitaentries', QiitaEntryViewSet, base_name='qiitaentries')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(users_router.urls)),
]