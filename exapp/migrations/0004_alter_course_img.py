# Generated by Django 3.2.7 on 2022-11-08 05:18

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('exapp', '0003_course_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='img',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to=''),
        ),
    ]
