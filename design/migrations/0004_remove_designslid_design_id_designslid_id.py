# Generated by Django 4.0.4 on 2022-07-05 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0003_remove_designslid_id_designslid_design_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designslid',
            name='design_id',
        ),
        migrations.AddField(
            model_name='designslid',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
