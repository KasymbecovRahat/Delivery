# Generated by Django 5.1.3 on 2024-12-01 06:39

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, unique=True)),
                ('category_name_ru', models.CharField(max_length=20, null=True, unique=True)),
                ('category_name_en', models.CharField(max_length=20, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('user_role', models.CharField(choices=[('Владелец', 'Владелец'), ('Клиент', 'Клиент'), ('Курьер', 'Курьер')], default='Клиент', max_length=12)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CourierReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Рейтинг')),
                ('client_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_review', to=settings.AUTH_USER_MODEL)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier_review', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders_status', models.CharField(choices=[('Ожидает  обработки', 'Ожидает  обработки'), ('В процессе доставки', 'В процессе доставки'), ('Доставлен', 'Доставлен'), ('Отменен', 'Отменен')], default='Ожидает  обработки', max_length=20)),
                ('orders_created', models.DateTimeField(auto_now_add=True)),
                ('delivery_address', models.CharField(max_length=64)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_project.cart')),
                ('client_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_orders', to=settings.AUTH_USER_MODEL)),
                ('courier_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier_orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_courier', models.CharField(choices=[('Доступен', 'Доступен'), ('Занят', 'Занят')], max_length=12)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('current_orders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courier', to='delivery_project.orders')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_name_ru', models.CharField(max_length=30, null=True)),
                ('product_name_en', models.CharField(max_length=30, null=True)),
                ('product_description', models.TextField()),
                ('product_description_ru', models.TextField(null=True)),
                ('product_description_en', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_photo', models.ImageField(upload_to='product_image/')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='delivery_project.category')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_product', to='delivery_project.product'),
        ),
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='delivery_project.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery_project.product')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=20)),
                ('store_name_ru', models.CharField(max_length=20, null=True)),
                ('store_name_en', models.CharField(max_length=20, null=True)),
                ('store_description', models.TextField(blank=True, null=True)),
                ('store_description_ru', models.TextField(blank=True, null=True)),
                ('store_description_en', models.TextField(blank=True, null=True)),
                ('store_image', models.ImageField(upload_to='store_photo')),
                ('address', models.CharField(max_length=50)),
                ('address_ru', models.CharField(max_length=50, null=True)),
                ('address_en', models.CharField(max_length=50, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_store', to='delivery_project.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCombo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('combo_name', models.CharField(max_length=30)),
                ('combo_name_ru', models.CharField(max_length=30, null=True)),
                ('combo_name_en', models.CharField(max_length=30, null=True)),
                ('combo_description', models.TextField()),
                ('combo_description_ru', models.TextField(null=True)),
                ('combo_description_en', models.TextField(null=True)),
                ('combo_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('combo_photo', models.ImageField(upload_to='combo_image/')),
                ('combo_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_combo', to='delivery_project.store')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='delivery_project.store'),
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='delivery_project.store')),
            ],
        ),
        migrations.CreateModel(
            name='StoreReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], verbose_name='Рейтинг')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_store', to='delivery_project.store')),
            ],
        ),
    ]
