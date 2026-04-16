from django.db import models

class Solicitud(models.Model):
    TIPOS = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]
    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS)
    asunto = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_solicitud = models.DateField()
    archivo = models.FileField(upload_to='solicitudes/', blank=True, null=True)