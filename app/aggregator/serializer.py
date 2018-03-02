from rest_framework import serializers

from accounts.models import User
from aggregator.models import QiitaEntry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class QiitaEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QiitaEntry
        fields = ('id', 'title', 'url', 'created_at', 'user')
