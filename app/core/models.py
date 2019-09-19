from django.db import models

class WhatsappGroup(models.Model):
    """The Whatsapp group model"""

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    invite_link = models.CharField(max_length=255)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        """String representation of the WhatsappGroup model"""

        return self.name


class Tag(models.Model):
    """The Whatsapp group tag model"""

    name = models.CharField(max_length=255)

    def __str__(self):
        """String representation of the Tag model"""

        return self.name
