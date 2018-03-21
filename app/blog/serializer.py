from rest_framework import serializers

from blog.models import BlogEntry


class BlogEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogEntry
        fields = ('id', 'title', 'content', 'created_at', 'category', 'user')
