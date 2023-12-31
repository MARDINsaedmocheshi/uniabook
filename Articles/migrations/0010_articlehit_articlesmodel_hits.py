# Generated by Django 4.2.6 on 2023-11-25 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0009_remove_articlesmodel_hits'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleHit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.articlesmodel')),
                ('ip_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Articles.ipaddress')),
            ],
        ),
        migrations.AddField(
            model_name='articlesmodel',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='Articles.ArticleHit', to='Articles.ipaddress', verbose_name='بازدید ها'),
        ),
    ]
