# Generated by Django 5.0 on 2024-01-01 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="marital_status",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Single", "Single"),
                    ("Married", "Married"),
                    ("Separated", "Separated"),
                    ("Divorced", "Divorced"),
                    ("Widowed", "Widowed"),
                    ("Stable Bond", "Stable Bond"),
                    ("Other", "Other"),
                ],
                max_length=255,
                null=True,
                verbose_name="marital status",
            ),
        ),
    ]