from django.db import models

# Create your models here.


class Gasto(models.Model):
    CATEGORIAS = [
        ("M", "Medicamentos"),
        ("S", "Supermercado"),
        ("E", "Empleados/as"),
        ("V", "Servicios"),
        ("C", "Comprobantes"),
        ("O", "Otros"),
    ]

    CUENTAS = [
        ("J", "Jubilacion"),
        ("V", "Vero"),
        ("M", "Moni"),
        ("G", "Gerardo"),
        ("W", "Walter"),
    ]

    MESES = [
        ("E", "Enero"),
        ("F", "Febrero"),
        ("M", "Marzo"),
        ("A", "Abril"),
        ("m", "Mayo"),
        ("J", "Junio"),
        ("j", "Julio"),
        ("a", "Agosto"),
        ("S", "Septiembre"),
        ("O", "Octubre"),
        ("N", "Noviembre"),
        ("D", "Diciembre"),
    ]

    nombre = models.CharField(max_length=13, null=False, blank=False)
    monto = models.IntegerField(null=False, blank=False,)
    categoria = models.CharField(
        max_length=1, null=False, blank=False, choices=CATEGORIAS
    )
    cuenta = models.CharField(max_length=1, null=False, blank=False, choices=CUENTAS)
    mes = models.CharField(max_length=1, null=False, blank=False, choices=MESES)
    comprobante = models.ImageField(upload_to="comprobantes", blank=False)


class Jubilacion(models.Model):
    MESES = [
        ("E", "Enero"),
        ("F", "Febrero"),
        ("M", "Marzo"),
        ("A", "Abril"),
        ("m", "Mayo"),
        ("J", "Junio"),
        ("j", "Julio"),
        ("a", "Agosto"),
        ("S", "Septiembre"),
        ("O", "Octubre"),
        ("N", "Noviembre"),
        ("D", "Diciembre"),
    ]

    total = models.IntegerField(null=False, blank=False)
    mes = models.CharField(max_length=1, null=False, blank=False, choices=MESES)
