from django.conf import settings

from file.models import File


def handle_uploaded_file(f_id):
    file = File.objects.get(id=f_id)
    file.processed = True
    file.save()
