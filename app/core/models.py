from django.db import models

class WhatsappGroup(models.Model):
    """The Whatsapp group model"""

    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    invite_link = models.CharField(max_length=255)

    def __str__(self):
        """String representation of the WhatsappGroupModel"""

        return self.name
