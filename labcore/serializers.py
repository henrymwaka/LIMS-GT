from rest_framework import serializers
from .models import (
    Gene, Vector, Primer, Construct, PCRRun,
    TransformationEvent, PlantLine, PCRConfirmation,
    Protocol, ExperimentLog
)

# ─── Gene Constructs & Related Models ─────────────────────────────

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
    gene_name = serializers.CharField(source='gene.name', read_only=True)
    vector_name = serializers.CharField(source='vector.name', read_only=True)

    class Meta:
        model = Construct
        fields = '__all__'

# ─── Experimental Records ─────────────────────────────────────────

class PCRRunSerializer(serializers.ModelSerializer):
    forward_primer_name = serializers.CharField(source='forward_primer.name', read_only=True)
    reverse_primer_name = serializers.CharField(source='reverse_primer.name', read_only=True)

    class Meta:
        model = PCRRun
        fields = '__all__'


class TransformationEventSerializer(serializers.ModelSerializer):
    construct_name = serializers.CharField(source='construct.name', read_only=True)

    class Meta:
        model = TransformationEvent
        fields = '__all__'


class PlantLineSerializer(serializers.ModelSerializer):
    construct_name = serializers.CharField(source='transformation_event.construct.name', read_only=True)
    event_id = serializers.CharField(source='transformation_event.id', read_only=True)

    class Meta:
        model = PlantLine
        fields = '__all__'


class PCRConfirmationSerializer(serializers.ModelSerializer):
    plant_id = serializers.CharField(source='plant_line.line_code', read_only=True)

    class Meta:
        model = PCRConfirmation
        fields = '__all__'

# ─── Protocols & Logs ────────────────────────────────────────────

class ProtocolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protocol
        fields = '__all__'


class ExperimentLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentLog
        fields = '__all__'
