# Generated by Django 2.1 on 2019-02-17 05:27

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0026_auto_20190217_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='image',
            field=models.FileField(max_length=256, upload_to=login.models.screenshot_directory_path),
        ),
    ]