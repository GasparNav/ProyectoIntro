# Generated by Django 2.2.3 on 2021-12-01 01:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('PRIMERA', '0008_auto_20211123_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('texto', models.TextField()),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved_comment', models.BooleanField(default=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='PRIMERA.material')),
            ],
        ),
    ]
