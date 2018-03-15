from rest_framework import serializers

from aggregator.models import QiitaEntry


class QiitaEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QiitaEntry
        fields = ('id', 'title', 'url', 'created_at', 'user')
