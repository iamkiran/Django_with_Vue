from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField()

    class Meta:
        model = News
        fields = ('title', 'author_Detail', 'date', 'm_image', 's_image', 'body')

