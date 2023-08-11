# Generated by Django 4.2.3 on 2023-08-11 09:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myzloo', '0018_alter_customuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='myzloo.musictrack')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('attachment', models.FileField(blank=True, null=True, upload_to='<django.db.models.fields.related.ForeignKey>/files')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='myzloo.musictrack')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(1, 'Too bad'), (2, 'Bad'), (3, 'Normal'), (4, 'Good'), (5, 'Excellent')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to=settings.AUTH_USER_MODEL)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='myzloo.musictrack')),
            ],
            options={
                'unique_together': {('owner', 'track')},
            },
        ),
    ]
