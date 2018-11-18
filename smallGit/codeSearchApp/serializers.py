from rest_framework import serializers
from .models import SearchHistory


class SearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'search_category',
            'search_query',
            'search_date'
        )
        model = SearchHistory
