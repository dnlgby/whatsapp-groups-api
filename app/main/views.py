from rest_framework import viewsets, mixins

from core.models import WhatsappGroup
from main import serializers


class WhatsappGroupsViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    """Create and list whatsapp groups"""

    serializer_class = serializers.WhatsappGroupSerializer
    queryset = WhatsappGroup.objects.all()
