# Generated by Django 3.0.8 on 2022-07-08 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220708_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='magazine_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='magazinecontent_brand', to='api.MagazineContent'),
        ),
    ]
