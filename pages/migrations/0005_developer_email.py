# Generated by Django 2.2 on 2019-05-17 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_projects_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='email',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
