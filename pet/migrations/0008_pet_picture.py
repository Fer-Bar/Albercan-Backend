# Generated by Django 5.0.2 on 2024-03-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0007_pet_gender_pet_is_neutered'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='picture',
            field=models.ImageField(blank=True, help_text='Max size allowed: 20Mbs', null=True, upload_to='images/pet/', verbose_name='picture'),
        ),
    ]
