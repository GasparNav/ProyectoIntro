# Generated by Django 2.2.3 on 2021-11-18 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRIMERA', '0004_auto_20211117_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='fecha_subida',
            field=models.DateField(),
        ),
    ]
