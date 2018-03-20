from rest_framework import serializers

from blog.models import Entry


class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = QiitaEntry
        fields = ('id', 'title', 'url', 'created_at', 'user')
