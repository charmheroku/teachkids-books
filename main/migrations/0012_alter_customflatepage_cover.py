# Generated by Django 4.0.4 on 2022-04-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_customflatepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customflatepage',
            name='cover',
            field=models.ImageField(default='', null=True, upload_to='flatpages', verbose_name='Image for page'),
        ),
    ]
