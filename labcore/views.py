from rest_framework import viewsets
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
    queryset = Construct.objects.select_related('gene', 'vector').prefetch_related('primers')
    serializer_class = ConstructSerializer


class PCRRunViewSet(viewsets.ModelViewSet):
    queryset = PCRRun.objects.select_related('construct')
    serializer_class = PCRRunSerializer


class TransformationEventViewSet(viewsets.ModelViewSet):
    queryset = TransformationEvent.objects.select_related('construct')
    serializer_class = TransformationEventSerializer


class PlantLineViewSet(viewsets.ModelViewSet):
    queryset = PlantLine.objects.select_related('transformation_event')
    serializer_class = PlantLineSerializer


class PCRConfirmationViewSet(viewsets.ModelViewSet):
    queryset = PCRConfirmation.objects.select_related('plant_line', 'primer')
    serializer_class = PCRConfirmationSerializer


class ProtocolViewSet(viewsets.ModelViewSet):
    queryset = Protocol.objects.all()
    serializer_class = ProtocolSerializer


class ExperimentLogViewSet(viewsets.ModelViewSet):
    queryset = ExperimentLog.objects.select_related('protocol', 'plant_line')
    serializer_class = ExperimentLogSerializer
