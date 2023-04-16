# Generated by Django 3.2 on 2023-03-03 16:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0003_auto_20230303_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(help_text='Автор отзыва', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, help_text='Дата публикации отзыва', verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(help_text='Отзыв о произведениии', verbose_name='Отзыв'),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.ForeignKey(help_text='Автор отзыва', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
    ]
