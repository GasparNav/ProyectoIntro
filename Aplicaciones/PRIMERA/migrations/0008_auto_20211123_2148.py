# Generated by Django 2.2.3 on 2021-11-24 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRIMERA', '0007_auto_20211123_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='archivo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
