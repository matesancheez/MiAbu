# Generated by Django 4.2.3 on 2023-07-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("usuario", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="gasto",
            name="descripcion",
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
    ]