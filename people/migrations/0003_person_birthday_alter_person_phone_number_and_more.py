# Generated by Django 5.0 on 2024-01-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("people", "0002_person_marital_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="birthday",
            field=models.DateField(blank=True, null=True, verbose_name="birthday"),
        ),
        migrations.AlterField(
            model_name="person",
            name="phone_number",
            field=models.CharField(
                blank=True,
                help_text="+591 70101010 (spaces are optional)",
                max_length=255,
                verbose_name="phone number",
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="secondary_phone_number",
            field=models.CharField(
                blank=True,
                help_text="+591 70101010 (spaces are optional)",
                max_length=255,
                null=True,
                verbose_name="secondary phone number",
            ),
        ),
    ]
