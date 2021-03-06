# Generated by Django 4.0.4 on 2022-06-09 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignSlid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design_img', models.ImageField(upload_to='slid_img')),
                ('design_title', models.CharField(max_length=200, verbose_name='Загаловок')),
                ('design_text', models.CharField(max_length=200, verbose_name='Текст')),
                ('design_css', models.CharField(default='-', max_length=200, null=True, verbose_name='CSS класс')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]
