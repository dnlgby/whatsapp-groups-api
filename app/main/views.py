from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from core.models import WhatsappGroup, Tag
from main import serializers
from rest_framework import pagination


class WhatsappGroupViewSet(viewsets.ModelViewSet):
    """Create and list whatsapp groups"""

    serializer_class = serializers.WhatsappGroupSerializer
    pagination_class = PageNumberPagination
    queryset = WhatsappGroup.objects.all()
    page_size_query_param = 'page_size'
    # If we want the 'Retrieve Model' to provide us details with another
    # field (instead of the default id field), we can change this var.
    # lookup_field = 'name'

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    # http://127.0.0.1:8000/api/groups/?tags=1
    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        tags = self.request.query_params.get('tags')

        queryset = self.queryset
        if tags:
            tag_ids = self._params_to_ints(tags)
            queryset = queryset.filter(tags__id__in=tag_ids)

        # If we want to add another query param.
        # if names:
        #     names = names.split(',')
        #     queryset = queryset.filter(name__name__in=names)

        # Remove duplicates
        return queryset.distinct()



class TagViewSet(viewsets.GenericViewSet,
                 mixins.ListModelMixin):
    """Manage Groups tags"""

    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    pagination.PageNumberPagination.page_size = 10
