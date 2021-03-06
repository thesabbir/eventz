# Generated by Django 3.2.3 on 2021-05-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
        ('orders', '0001_initial'),
        ('events', '0002_event_merchandises'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='tags.Tag'),
        ),
    ]
