from rest_framework import viewsets

from blog.models import Entry
from blog.serializer import EntrySerializer


class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    http_method_names = ['get', 'head', 'options']

    def get_queryset(self):
        return Entry.objects.filter(user=self.kwargs['user_pk'])
