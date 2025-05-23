from rest_framework import routers
from livreAPI.views import LivreViewSet
from .views import LivreListView
from django.urls import path

router = routers.DefaultRouter()
router.register('livre', LivreViewSet)


urlpatterns = [
    path('livres/', LivreListView.as_view(), name='livre-list'),
]

