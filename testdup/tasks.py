from celery import shared_task

from file.handle import handle_uploaded_file


@shared_task()
def handle_uploaded_file_task(f_id):
    return handle_uploaded_file(f_id)
