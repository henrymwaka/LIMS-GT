from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'genes', views.GeneViewSet)
router.register(r'vectors', views.VectorViewSet)
router.register(r'primers', views.PrimerViewSet)
router.register(r'constructs', views.ConstructViewSet)
router.register(r'pcr-runs', views.PCRRunViewSet)
router.register(r'transformations', views.TransformationEventViewSet)
router.register(r'plant-lines', views.PlantLineViewSet)
router.register(r'pcr-confirmations', views.PCRConfirmationViewSet)
router.register(r'protocols', views.ProtocolViewSet)
router.register(r'experiment-logs', views.ExperimentLogViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Custom endpoints
    path('summary-stats/', views.summary_stats, name='summary-stats'),
    path('plant-lines/by-event/<int:event_id>/', views.plant_lines_by_event, name='plant-lines-by-event'),
]
