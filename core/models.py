from django.db import models

class EditorialStyleSheet(models.Model):
    """
    Global rules for the organization.
    """
    name = models.CharField(max_length=255)
    rules = models.TextField(help_text="Global rules for the organization")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
