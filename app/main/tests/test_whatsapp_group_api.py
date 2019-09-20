from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import WhatsappGroup
from main.serializers import WhatsappGroupSerializer


WHATSAPPGROUP_URL = reverse('main:whatsappgroup-list')


class PublicWhatsappGroupclassAPITests(TestCase):
    """Tests for the public WhatsappGroup API"""

    def setUp(self):
        self.client = APIClient()

    def test_retrieve_groups(self):
        """Test that groups is retreived"""

        WhatsappGroup.objects.create(
            name='group1',
            description='description1',
            invite_link='invite_link1'
        )

        WhatsappGroup.objects.create(
            name='group2',
            description='description2',
            invite_link='invite_link2'
        )

        res = self.client.get(WHATSAPPGROUP_URL)

        all_groups = WhatsappGroup.objects.all()
        serializer = WhatsappGroupSerializer(all_groups, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['results'], serializer.data)
