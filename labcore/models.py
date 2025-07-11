from django.db import models
from django.contrib.auth.models import User

# ──────────────── Reference Models ────────────────

class Gene(models.Model):
    name = models.CharField(max_length=100)
    accession_number = models.CharField(max_length=100, blank=True, null=True)
    organism = models.CharField(max_length=100)
    function = models.TextField()
    sequence_file = models.FileField(upload_to='genes/sequences/', blank=True, null=True)

    def __str__(self):
        return self.name


class Vector(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, help_text="e.g., binary, plasmid")
    antibiotic_resistance = models.CharField(max_length=100)
    map_file = models.FileField(upload_to='vectors/maps/', blank=True, null=True)

    def __str__(self):
        return self.name


class Primer(models.Model):
    name = models.CharField(max_length=100)
    sequence = models.TextField()
    melting_temp = models.FloatField()
    product_size_bp = models.IntegerField()
    supplier = models.CharField(max_length=100)
    lot_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

# ──────────────── Experimental Pipeline ────────────────

class Construct(models.Model):
    name = models.CharField(max_length=100)
    gene = models.ForeignKey(Gene, on_delete=models.CASCADE)
    vector = models.ForeignKey(Vector, on_delete=models.CASCADE)
    cloning_method = models.CharField(max_length=100, help_text="e.g., Gibson, TA, Gateway")
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class PCRRun(models.Model):
    construct = models.ForeignKey(Construct, on_delete=models.CASCADE)
    forward_primer = models.ForeignKey(Primer, related_name='fwd_pcrs', on_delete=models.CASCADE)
    reverse_primer = models.ForeignKey(Primer, related_name='rev_pcrs', on_delete=models.CASCADE)
    enzyme = models.CharField(max_length=100)
    annealing_temp = models.FloatField()
    cycles = models.IntegerField()
    buffer = models.CharField(max_length=100)
    success = models.BooleanField()
    notes = models.TextField(blank=True)
    gel_image = models.ImageField(upload_to='pcr/gels/', blank=True, null=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.construct.name} - PCR {self.date}"


class TransformationEvent(models.Model):
    construct = models.ForeignKey(Construct, on_delete=models.CASCADE)
    method = models.CharField(max_length=100, help_text="e.g., Agrobacterium, Electroporation")
    competent_strain = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    efficiency_percent = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.construct.name} - {self.method} ({self.date})"


class PlantLine(models.Model):
    line_code = models.CharField(max_length=100, unique=True)
    transformation_event = models.ForeignKey(TransformationEvent, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=[
        ('callus', 'Callus'),
        ('shoot', 'Shoot'),
        ('rooted', 'Rooted'),
        ('acclimatized', 'Acclimatized'),
        ('lost', 'Lost'),
        ('confirmed', 'Confirmed'),
    ])
    image = models.ImageField(upload_to='plant_lines/', blank=True, null=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.line_code


class PCRConfirmation(models.Model):
    plant_line = models.ForeignKey(PlantLine, on_delete=models.CASCADE)
    primers_used = models.ManyToManyField(Primer)
    result = models.CharField(max_length=100, choices=[
        ('positive', 'Positive'),
        ('negative', 'Negative'),
        ('inconclusive', 'Inconclusive')
    ])
    gel_image = models.ImageField(upload_to='confirmations/gels/', blank=True, null=True)
    notes = models.TextField(blank=True)
    confirmed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.plant_line.line_code} - {self.result}"

# ──────────────── Protocol & Supervision ────────────────

class Protocol(models.Model):
    title = models.CharField(max_length=200)
    version = models.CharField(max_length=20)
    description = models.TextField()
    document = models.FileField(upload_to='protocols/')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} (v{self.version})"


class ExperimentLog(models.Model):
    project_title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.TextField()
    protocol_used = models.ForeignKey(Protocol, on_delete=models.SET_NULL, null=True, blank=True)
    date_logged = models.DateTimeField(auto_now_add=True)
    flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.project_title} - {self.user.username} ({self.date_logged.strftime('%Y-%m-%d')})"
