# Generated by Django 4.0.4 on 2022-07-05 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designslid',
            options={'verbose_name': 'Портфолио', 'verbose_name_plural': 'Портфолио img'},
        ),
        migrations.RemoveField(
            model_name='designslid',
            name='design_text',
        ),
    ]
