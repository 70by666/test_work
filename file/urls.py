from django.urls import include, path
from rest_framework import routers

from .views import FileViewSet, AddFile

router = routers.DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('upload/', AddFile.as_view())
]
