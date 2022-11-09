# Generated by Django 4.1.2 on 2022-11-09 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Sensor",
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
                ("name", models.TextField(max_length=25)),
                ("description", models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Measurement",
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
                ("temperature", models.FloatField()),
                ("measured_at", models.DateField(auto_now=True)),
                ("image", models.ImageField(null=True, upload_to="media")),
                (
                    "sensor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="measurements",
                        to="measurement.sensor",
                    ),
                ),
            ],
        ),
    ]
