from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main import views

app_name = 'main'


router = DefaultRouter()
router.register('groups', views.WhatsappGroupsViewSet)
router.register('tags', views.TagViewSet)


urlpatterns = [
    path('', include(router.urls))
]
