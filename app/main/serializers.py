from rest_framework import serializers

from core.models import WhatsappGroup

class WhatsappGroupSerializer(serializers.ModelSerializer):
    """Serializer for WhatsappGroup objects"""

    class Meta:
        model = WhatsappGroup
        fields = ('name', 'description', 'invite_link')
