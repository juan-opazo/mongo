"""
Serializers for tweet APIs
"""
from rest_framework import serializers

from core.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    """Serializer for tweets."""

    class Meta:
        model = Tweet
        fields = ['id', 'content', 'label']
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a new tweet instance"""
        tweet = Tweet.objects.create(**validated_data)
        return tweet


class TweetDetailSerializer(TweetSerializer):
    """Serializers for tweet details."""

    class Meta(TweetSerializer.Meta):
        fields = TweetSerializer.Meta.fields
