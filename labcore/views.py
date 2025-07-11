from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import *
from .serializers import *

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
    queryset = Construct.objects.all()
    serializer_class = ConstructSerializer

class PCRRunViewSet(viewsets.ModelViewSet):
    queryset = PCRRun.objects.all()
    serializer_class = PCRRunSerializer

class TransformationEventViewSet(viewsets.ModelViewSet):
    queryset = TransformationEvent.objects.all()
    serializer_class = TransformationEventSerializer

class PlantLineViewSet(viewsets.ModelViewSet):
    queryset = PlantLine.objects.all()
    serializer_class = PlantLineSerializer

class PCRConfirmationViewSet(viewsets.ModelViewSet):
    queryset = PCRConfirmation.objects.all()
    serializer_class = PCRConfirmationSerializer

class ProtocolViewSet(viewsets.ModelViewSet):
    queryset = Protocol.objects.all()
    serializer_class = ProtocolSerializer

class ExperimentLogViewSet(viewsets.ModelViewSet):
    queryset = ExperimentLog.objects.all()
    serializer_class = ExperimentLogSerializer
