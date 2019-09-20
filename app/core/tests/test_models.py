from django.test import TestCase

from core import models


class ModelTests(TestCase):
    """Class containing tests for the core app models"""

    def test_whatsappgroup_string_representation(self):
        """Test the WhatsappGroup model string representation"""

        whatsappgroup = models.WhatsappGroup.objects.create(
            name="Group_1",
            description="Group_1 Desctiption",
            invite_link="Group_1 Invite link"
        )

        self.assertEqual(str(whatsappgroup), whatsappgroup.name)

    def test_tag_string_representation(self):
        """Test the Tag model string representation"""

        tag = models.Tag.objects.create(
            name="Tag_1"
        )

        self.assertEqual(str(tag), tag.name)
