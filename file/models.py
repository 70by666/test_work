from django.db import models
from django.conf import settings


class File(models.Model):
    objects = models.Manager()
    file = models.FileField(upload_to=f'{settings.BASE_DIR}/files')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
