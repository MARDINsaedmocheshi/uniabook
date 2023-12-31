# Generated by Django 4.2.6 on 2023-11-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0006_alter_articlesmodel_body_or_text_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlesmodel',
            name='is_special',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
        migrations.AlterField(
            model_name='articlesmodel',
            name='status_Article',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر'), ('m', 'تعداد مقاله محدود'), ('f', 'مقاله موجود نیست'), ('n', 'حذف خواهد شد'), ('b', 'به زودی موجود خواهد شد'), ('r', 'به دلیل عمل نکردن به قوانین سایت رد شد'), ('i', ' در حال بررسی'), ('j', ' برگشت داده شده')], default='d', max_length=1, verbose_name='  وضعیت انتشار مقاله'),
        ),
    ]
