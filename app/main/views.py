from rest_framework import viewsets, mixins

from core.models import WhatsappGroup, Tag
from main import serializers


class WhatsappGroupsViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin):
    """Create and list whatsapp groups"""

    serializer_class = serializers.WhatsappGroupSerializer
    queryset = WhatsappGroup.objects.all()


    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    # http://127.0.0.1:8000/api/recipe/recipes/?tags=2&ingredients=3
    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        tags = self.request.query_params.get('tags')

        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        # Remove duplicates
        return queryset.distinct()


class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin):
    """Manage Groups tags"""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
