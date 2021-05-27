from rest_framework import serializers
from quoteapp.models import Quote


class QuoteDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = "__all__"