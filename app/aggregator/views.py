from rest_framework import viewsets

from aggregator.models import QiitaEntry
from aggregator.serializer import QiitaEntrySerializer


class QiitaEntryViewSet(viewsets.ModelViewSet):
    serializer_class = QiitaEntrySerializer
    http_method_names = ['get', 'head', 'options']

    def get_queryset(self):
        return QiitaEntry.objects.filter(user=self.kwargs['user_pk'])
