from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GeneViewSet, VectorViewSet, PrimerViewSet, ConstructViewSet,
    PCRRunViewSet, TransformationEventViewSet, PlantLineViewSet,
    PCRConfirmationViewSet, ProtocolViewSet, ExperimentLogViewSet
)

# Create router and register viewsets
router = DefaultRouter()
router.register(r'genes', GeneViewSet, basename='gene')
router.register(r'vectors', VectorViewSet, basename='vector')
router.register(r'primers', PrimerViewSet, basename='primer')
router.register(r'constructs', ConstructViewSet, basename='construct')
router.register(r'pcr-runs', PCRRunViewSet, basename='pcr-run')
router.register(r'transformations', TransformationEventViewSet, basename='transformation')
router.register(r'plant-lines', PlantLineViewSet, basename='plant-line')
router.register(r'pcr-confirmations', PCRConfirmationViewSet, basename='pcr-confirmation')
router.register(r'protocols', ProtocolViewSet, basename='protocol')
router.register(r'experiment-logs', ExperimentLogViewSet, basename='experiment-log')

# Wire up API
urlpatterns = [
    path('', include(router.urls)),
]
