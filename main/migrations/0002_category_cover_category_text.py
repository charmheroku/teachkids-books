# Generated by Django 4.0.4 on 2022-04-22 12:45

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cover',
            field=models.ImageField(default='', upload_to='categories', verbose_name='Image for category'),
        ),
        migrations.AddField(
            model_name='category',
            name='text',
            field=ckeditor.fields.RichTextField(default='', verbose_name='Text'),
        ),
    ]
