from rest_framework import serializers
from .models import (
    Gene, Vector, Primer, Construct, PCRRun,
    TransformationEvent, PlantLine, PCRConfirmation,
    Protocol, ExperimentLog
)

class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = '__all__'

class VectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vector
        fields = '__all__'

class PrimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Primer
        fields = '__all__'

class ConstructSerializer(serializers.ModelSerializer):
    class Meta:
        model = Construct
        fields = '__all__'

class PCRRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCRRun
        fields = '__all__'

class TransformationEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransformationEvent
        fields = '__all__'

class PlantLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantLine
        fields = '__all__'

class PCRConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PCRConfirmation
        fields = '__all__'

class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol
        fields = '__all__'

class ExperimentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentLog
        fields = '__all__'
