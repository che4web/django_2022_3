# Generated by Django 3.2.7 on 2022-11-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='exersise',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название упражнениея'),
        ),
    ]