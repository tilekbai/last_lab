from rest_framework import serializers
from quoteapp.models import Quote


class QuoteDetailSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Quote
        fields = ("text", "name", "email", "rating", "status", "created")
        read_only_fields = ("rating", "status", "created")


class QuoteListSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Quote
        fields = ("id", "created", "text", "rating")