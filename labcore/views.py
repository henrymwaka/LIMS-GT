from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Count

from .models import (
    Gene, Vector, Primer, Construct, PCRRun,
    TransformationEvent, PlantLine, PCRConfirmation,
    Protocol, ExperimentLog
)

from .serializers import (
    GeneSerializer, VectorSerializer, PrimerSerializer,
    ConstructSerializer, PCRRunSerializer, TransformationEventSerializer,
    PlantLineSerializer, PCRConfirmationSerializer,
    ProtocolSerializer, ExperimentLogSerializer
)


# ─── ViewSets ────────────────────────────────────────────────

class GeneViewSet(viewsets.ModelViewSet):
    queryset = Gene.objects.all()
    serializer_class = GeneSerializer

class VectorViewSet(viewsets.ModelViewSet):
    queryset = Vector.objects.all()
    serializer_class = VectorSerializer

class PrimerViewSet(viewsets.ModelViewSet):
    queryset = Primer.objects.all()
    serializer_class = PrimerSerializer

class ConstructViewSet(viewsets.ModelViewSet):
    queryset = Construct.objects.select_related('gene', 'vector')
    serializer_class = ConstructSerializer

class PCRRunViewSet(viewsets.ModelViewSet):
    queryset = PCRRun.objects.select_related('construct', 'forward_primer', 'reverse_primer')
    serializer_class = PCRRunSerializer

class TransformationEventViewSet(viewsets.ModelViewSet):
    queryset = TransformationEvent.objects.select_related('construct')
    serializer_class = TransformationEventSerializer

class PlantLineViewSet(viewsets.ModelViewSet):
    queryset = PlantLine.objects.select_related('transformation_event')
    serializer_class = PlantLineSerializer

class PCRConfirmationViewSet(viewsets.ModelViewSet):
    queryset = PCRConfirmation.objects.select_related('plant_line').prefetch_related('primers_used')
    serializer_class = PCRConfirmationSerializer

class ProtocolViewSet(viewsets.ModelViewSet):
    queryset = Protocol.objects.select_related('created_by')
    serializer_class = ProtocolSerializer

class ExperimentLogViewSet(viewsets.ModelViewSet):
    queryset = ExperimentLog.objects.select_related('protocol', 'user')
    serializer_class = ExperimentLogSerializer


# ─── Custom API Views ────────────────────────────────────────

@api_view(['GET'])
@permission_classes([AllowAny])
def summary_stats(request):
    stats = {
        "gene_count": Gene.objects.count(),
        "vector_count": Vector.objects.count(),
        "primer_count": Primer.objects.count(),
        "construct_count": Construct.objects.count(),
        "pcr_run_count": PCRRun.objects.count(),
        "transformation_events": TransformationEvent.objects.count(),
        "plant_lines": PlantLine.objects.count(),
    }
    return Response(stats)

@api_view(['GET'])
@permission_classes([AllowAny])
def plant_lines_by_event(request, event_id):
    lines = PlantLine.objects.filter(transformation_event__id=event_id).values('line_code', 'status')
    return Response({
        "event_id": event_id,
        "plant_lines": list(lines)
    })
