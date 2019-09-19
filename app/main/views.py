from rest_framework import generics

from main import serializers

class WhatsappGroupsView(generics.ListCreateAPIView):
    """Create and list whatsapp groups"""

    serializer_class = serializers.WhatsappGroupSerializer
