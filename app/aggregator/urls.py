from django.urls import path, include

from rest_framework_nested import routers
from rest_framework_swagger.views import get_swagger_view

from blog.views import BlogEntryViewSet, UserBlogEntryViewSet
from aggregator.views import QiitaEntryViewSet
from accounts.views import UserViewSet

schema_view = get_swagger_view(title='Blog Aggregator API')

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'blogentries', BlogEntryViewSet, base_name='blogentries')

users_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
users_router.register(r'qiitaentries', QiitaEntryViewSet, base_name='qiitaentries')
users_router.register(r'blogentries', UserBlogEntryViewSet, base_name='blogentries_per_user')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include(users_router.urls)),
    path('docs/', schema_view)
]
