# Generated by Django 3.1.2 on 2022-01-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]