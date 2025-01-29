
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from knowledgebase import views

app_name = 'knowledgebase'

router = DefaultRouter()
router.register(app_name, views.KnowledgeBaseViewSet, basename=app_name)


urlpatterns = [
        path('', include(router.urls))]









