from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter
from myapp.views import PersonViewSet,ColorViewSet

router = DefaultRouter()
router.register(r'persons', PersonViewSet )
router.register(r'colors', ColorViewSet)

urlpatterns = [
    path("",include(router.urls)),
]
