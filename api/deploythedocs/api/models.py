from django.db import models


class Version(models.Model):
    """Represent a version of documentation in a specific project."""
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    bundle = models.FileField()

    class Meta:
        managed = False  # What's on disk is our source of truth
