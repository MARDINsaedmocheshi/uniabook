# Generated by Django 4.2.6 on 2023-11-25 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0008_ipaddress_articlesmodel_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlesmodel',
            name='hits',
        ),
    ]