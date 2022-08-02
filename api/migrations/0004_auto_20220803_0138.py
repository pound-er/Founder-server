# Generated by Django 3.0.8 on 2022-08-03 01:38

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20220729_0200'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='brand_desc_detail',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='api.Product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_img_main',
            field=models.ImageField(blank=True, upload_to=api.models.review_path),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL),
        ),
    ]
