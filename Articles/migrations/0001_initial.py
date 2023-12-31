# Generated by Django 4.2.6 on 2023-10-18 09:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_category', models.CharField(max_length=200, verbose_name='عنوان دسته بندی ')),
                ('slug_category', models.SlugField(max_length=100, unique=True, verbose_name='آدرس دسته بندی')),
                ('status_category', models.BooleanField(default=True, verbose_name='آیا نمایش داده شود؟')),
                ('position_category', models.IntegerField(verbose_name='شماره دسته بندی')),
                ('publish_category', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار دسته بندی')),
                ('created_category', models.DateTimeField(auto_now_add=True, verbose_name='دسته بندی کی ایجاد شد؟')),
                ('updated_category', models.DateTimeField(auto_now=True, verbose_name='دسته بندی کی آپدیت شد؟')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='Articles.category', verbose_name='دسته بندی والد | زیر دسته')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['parent__id', 'position_category'],
            },
        ),
    ]
