# Generated by Django 3.0.8 on 2022-07-23 15:59

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nickname', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('gender', models.CharField(choices=[('female', 'female'), ('male', 'male')], max_length=20)),
                ('set_curation', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', api.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=20)),
                ('brand_logo', models.ImageField(null=True, upload_to=api.models.brand_path)),
                ('brand_link', models.URLField()),
                ('brand_desc', models.TextField()),
                ('brand_bg_img', models.ImageField(null=True, upload_to=api.models.brand_path)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(choices=[('food', 'food'), ('beverage', 'beverage'), ('goods', 'goods'), ('health', 'health')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('tag_arr', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('episode_num', models.IntegerField(blank=True, null=True)),
                ('main_img', models.ImageField(blank=True, null=True, upload_to=api.models.magazine_path)),
                ('header_img', models.ImageField(blank=True, null=True, upload_to=api.models.magazine_path)),
                ('magazine_type', models.CharField(choices=[('founder-story', 'founder-story'), ('daily-curation', 'daily-curation')], max_length=20)),
                ('intro_content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_main_img', models.ImageField(null=True, upload_to=api.models.product_path)),
                ('product_detail_img', models.ImageField(null=True, upload_to=api.models.product_path)),
                ('custom_flag', models.BooleanField(default=False)),
                ('delivery_cycle_main', models.CharField(choices=[('weekly', 'weekly'), ('monthly', 'monthly'), ('weekly/monthly', 'weekly/monthly')], max_length=20)),
                ('delivery_cycle_detail', models.TextField()),
                ('min_price', models.IntegerField()),
                ('star_rate_avg', models.FloatField(default=0.0)),
                ('min_std_price', models.FloatField()),
                ('max_std_price', models.FloatField()),
                ('discount_flag', models.BooleanField()),
                ('purchase_link', models.URLField()),
                ('main_product_flag', models.BooleanField()),
                ('default_rec_flag', models.BooleanField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_product', to='api.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rate', models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)])),
                ('review_text', models.TextField()),
                ('review_tag_arr', models.TextField()),
                ('review_main_img', models.ImageField(blank=True, null=True, upload_to=api.models.review_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_review', to='api.Product')),
                ('user', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_num', models.IntegerField()),
                ('answer_num', models.IntegerField()),
                ('type_arr', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(choices=[('milk', 'milk'), ('shake', 'shake'), ('yogurt', 'yogurt'), ('salad', 'salad'), ('fried-rice', 'fried-rice'), ('cereal', 'cereal'), ('bread', 'bread'), ('chicken', 'chicken'), ('coffee-cold', 'coffee-cold'), ('coffee-beans', 'coffee-beans'), ('coffee-capsule', 'coffee-capsule'), ('tea', 'tea'), ('pad', 'pad'), ('teeth', 'teeth'), ('pack', 'pack'), ('cotton', 'cotton'), ('lens', 'lens'), ('shaver', 'shaver'), ('lacto', 'lacto'), ('supplement', 'supplement'), ('skin-care-pack', 'skin-care-pack'), ('care-pack', 'care-pack'), ('protein', 'protein'), ('collagen', 'collagen')], max_length=20)),
                ('type_desc', models.CharField(max_length=100)),
                ('type_desc_detail', models.CharField(max_length=100)),
                ('type_tag_arr', models.TextField()),
                ('type_img', models.ImageField(upload_to=api.models.type_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_type', to='api.Category')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_result', models.BooleanField(default=False, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_surveyresult', to='api.Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_surveyresult', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_img', models.ImageField(blank=True, null=True, upload_to=api.models.review_media_path)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_reviewmedia', to='api.Review')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_product', to='api.Type'),
        ),
        migrations.CreateModel(
            name='MagazineContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_title', models.CharField(blank=True, max_length=100, null=True)),
                ('detail_content', models.TextField(blank=True, null=True)),
                ('detail_img', models.ImageField(blank=True, null=True, upload_to=api.models.magazine_path)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brand_magazinecontent', to='api.Brand')),
                ('magazine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='magazine_magazinecontent', to='api.Magazine')),
            ],
        ),
    ]