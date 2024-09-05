from django.db import models
from datetime import datetime

class Photos(models.Model):

    CATEGORY_CHOICES = [
        ("SPACE", "space"),
        ("ASTRONAUT", "astronaut")
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(max_length=150, choices=CATEGORY_CHOICES, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    visible = models.BooleanField(default=False)
    date_photo = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self) -> str:
        return self.name