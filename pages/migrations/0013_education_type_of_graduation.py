# Generated by Django 2.2 on 2019-05-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20190517_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='type_of_graduation',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
