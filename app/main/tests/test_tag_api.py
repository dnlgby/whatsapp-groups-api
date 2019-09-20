from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from main.serializers import TagSerializer

TAGS_URL = reverse('main:tag-list')


class PublicTagAPITests(TestCase):
    """Tests for the public TAG API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_tags(self):
        """Test that tags is retreived"""

        Tag.objects.create(name='tag_1')
        Tag.objects.create(name='tag_2')

        res = self.client.get(TAGS_URL)

        all_tags = Tag.objects.all()
        serializer = TagSerializer(all_tags, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'], serializer.data)

    def test_creating_tag_not_allowed(self):
        """Test creating a new tag is not allowed"""

        payload = {'name': 'tag_1'}
        res = self.client.post(TAGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
