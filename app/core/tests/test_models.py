from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Class containing tests for the core app models"""

    def test_whatsappgroup_string_representation(self):
        """Test the whatsappgroup string representation"""

        whatsappgroup = models.WhatsappGroup.objects.create(
            name="Group_1",
            description="Group_1 Desctiption",
            invite_link="Group_1 Invite link"
        )

        assertEqual(str(whatsappgroup), whatsappgroup.name)
