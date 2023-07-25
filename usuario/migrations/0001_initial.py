# Generated by Django 4.2.3 on 2023-07-19 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gasto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=13)),
                ("monto", models.IntegerField()),
                (
                    "categoria",
                    models.CharField(
                        choices=[
                            ("M", "Medicamentos"),
                            ("S", "Supermercado"),
                            ("E", "Empleados/as"),
                            ("S", "Servicios"),
                            ("O", "Otros"),
                        ],
                        max_length=1,
                    ),
                ),
                ("cuenta", models.CharField(max_length=10)),
                ("fecha", models.DateField()),
            ],
        ),
    ]
