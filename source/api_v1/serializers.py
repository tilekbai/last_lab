from rest_framework import serializers
from quoteapp.models import Quote


class QuoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("text", "name", "email")


class QuoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("id", "text", "name")