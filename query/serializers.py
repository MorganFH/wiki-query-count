from rest_framework import serializers


class QuerySerializer(serializers.Serializer):
    hits = serializers.IntegerField()
    topic = serializers.CharField(max_length=200)
    section = serializers.IntegerField()