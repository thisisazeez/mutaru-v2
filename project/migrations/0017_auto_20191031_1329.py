# Generated by Django 2.2.6 on 2019-10-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0016_auto_20191030_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='project',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]