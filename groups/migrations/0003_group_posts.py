# Generated by Django 2.0.9 on 2019-01-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('groups', '0002_group_u_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='posts',
            field=models.ManyToManyField(to='posts.Post'),
        ),
    ]