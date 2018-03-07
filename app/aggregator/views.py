from django.shortcuts import render

from rest_framework import viewsets

from accounts.models import User
from aggregator.models import QiitaEntry
from aggregator.serializer import UserSerializer, QiitaEntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QiitaEntryViewSet(viewsets.ModelViewSet):
    serializer_class = QiitaEntrySerializer

    def get_queryset(self):
        return QiitaEntry.objects.filter(user=self.kwargs['user_pk'])
