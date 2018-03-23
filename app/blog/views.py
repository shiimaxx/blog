from rest_framework import viewsets

from blog.models import BlogEntry
from blog.serializer import BlogEntrySerializer


class BlogEntryViewSet(viewsets.ModelViewSet):
    serializer_class = BlogEntrySerializer
    http_method_names = ['get', 'head', 'options', 'post', 'delete']

    def get_queryset(self):
        return BlogEntry.objects.filter(user=self.kwargs['user_pk'])
