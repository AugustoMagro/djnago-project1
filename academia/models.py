from django.db import models

class Photos(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        return f"Photos [name={self.name}]"