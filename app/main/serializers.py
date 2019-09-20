from rest_framework import serializers

from core.models import WhatsappGroup, Tag


class WhatsappGroupSerializer(serializers.ModelSerializer):
    """Serializer for WhatsappGroup objects"""

    class Meta:
        model = WhatsappGroup
        fields = ('id', 'name', 'description', 'invite_link', 'tags')
        read_only_fields = ('id',)


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
