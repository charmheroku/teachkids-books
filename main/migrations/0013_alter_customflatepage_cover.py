# Generated by Django 4.0.4 on 2022-04-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_customflatepage_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customflatepage',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='flatpages', verbose_name='Image for page'),
        ),
    ]
