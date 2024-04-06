# Generated by Django 5.0.1 on 2024-04-05 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='follow_requests',
            field=models.ManyToManyField(related_name='requests', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='followers',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
