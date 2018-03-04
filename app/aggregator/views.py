from django.shortcuts import render

from rest_framework import viewsets

from accounts.models import User
from aggregator.models import QiitaEntry
from aggregator.serializer import UserSerializer, QiitaEntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class QiitaEntryViewSet(viewsets.ModelViewSet):
    queryset = QiitaEntry.objects.all()
    serializer_class = QiitaEntrySerializer
