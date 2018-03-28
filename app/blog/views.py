from rest_framework import viewsets

from blog.models import BlogEntry
from blog.serializer import BlogEntrySerializer
from blog.permissions import IsOwnerOrReadOnly


class UserBlogEntryViewSet(viewsets.ModelViewSet):
    serializer_class = BlogEntrySerializer
    http_method_names = ['get', 'head', 'options']

    def get_queryset(self):
        return BlogEntry.objects.filter(user=self.kwargs['user_pk'])


class BlogEntryViewSet(viewsets.ModelViewSet):
    queryset = BlogEntry.objects.all()
    serializer_class = BlogEntrySerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete']
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
