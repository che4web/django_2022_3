# Generated by Django 3.2.7 on 2022-11-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stdapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chackpoint',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
