# Generated by Django 4.0.4 on 2022-05-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_sociallink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookfile',
            name='format_book',
            field=models.CharField(choices=[('1', 'Lesson Text'), ('2', 'Visuals'), ('3', 'Resource pack')], default='1', max_length=20),
        ),
    ]
