"""
Views for the Tweet APIs
"""
from rest_framework import viewsets

from core.models import Tweet
from tweet import serializers


class TweetViewSet(viewsets.ModelViewSet):
    """View for manage Tweet APIs"""
    serializer_class = serializers.TweetDetailSerializer
    queryset = Tweet.objects.all()

    def get_queryset(self):
        """Retrieve Tweets"""
        return self.queryset.order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request"""
        if self.action == 'list':
            return serializers.TweetSerializer

        return self.serializer_class

    def perform_create_serializer(self):
        """Create a new tweet"""
        serializers.save()
