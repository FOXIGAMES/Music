# Generated by Django 4.2.3 on 2023-07-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myzloo', '0011_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musictrack',
            name='duration_seconds',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]