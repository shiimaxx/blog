from rest_framework import serializers

from blog.models import BlogEntry


class BlogEntrySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = BlogEntry
        fields = ('id', 'title', 'content', 'created_at', 'category', 'user')

    def get_user(self, obj):
        return str(obj.user.username)
