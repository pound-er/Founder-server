# Generated by Django 3.0.8 on 2022-07-23 16:52

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='type_img',
            field=models.FileField(upload_to=api.models.type_path),
        ),
    ]
