# Generated by Django 4.2.3 on 2023-07-23 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myzloo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musictrack',
            name='duration_seconds',
            field=models.PositiveIntegerField(editable=False),
        ),
    ]
