from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main import views


router = DefaultRouter()
router.register('main', views.WhatsappGroupsViewSet)

app_name = 'main'

urlpatterns = [
    path('', include(router.urls))
]
