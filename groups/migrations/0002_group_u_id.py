# Generated by Django 2.0.9 on 2018-12-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='u_id',
            field=models.CharField(default=0, max_length=8),
        ),
    ]
