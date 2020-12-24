# Generated by Django 2.2.14 on 2020-11-29 16:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('address_type', models.CharField(choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='cal_cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_product', models.CharField(max_length=100)),
                ('Category_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='CATEGORY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_username', models.CharField(max_length=100, null=True)),
                ('stock', models.BooleanField(default=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static  ')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.CATEGORY')),
            ],
        ),
        migrations.CreateModel(
            name='signup2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name1', models.CharField(max_length=30)),
                ('user_email1', models.CharField(max_length=30)),
                ('user_phone_no1', models.CharField(max_length=30)),
                ('user_password1', models.CharField(max_length=30)),
                ('user_address1', models.CharField(max_length=300)),
                ('user_pincode1', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SUB_CATEGORY',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sub_Category', models.CharField(max_length=30)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_home.CATEGORY')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_customer_id', models.CharField(blank=True, max_length=50, null=True)),
                ('one_click_purchasing', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SUB_CATEGORY_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=30)),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_home.CATEGORY')),
                ('Sub_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SUB_CATEGORY')),
            ],
        ),
        migrations.CreateModel(
            name='SellerAccount_requested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('active', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SellerAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100, null=True)),
                ('active', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('managers', models.ManyToManyField(blank=True, related_name='manager_sellers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='seller_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Buisiness_Name', models.CharField(max_length=100, null=True)),
                ('GSTN', models.CharField(max_length=100, null=True)),
                ('Pancard_Number', models.CharField(max_length=100, null=True)),
                ('Pancard_Picture', models.ImageField(null=True, upload_to='static')),
                ('Owner_Name', models.CharField(max_length=100, null=True)),
                ('Address1', models.CharField(max_length=100, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('State', models.CharField(max_length=100, null=True)),
                ('Zip', models.CharField(max_length=100, null=True)),
                ('Address2', models.CharField(max_length=100, null=True)),
                ('City2', models.CharField(max_length=100, null=True)),
                ('State2', models.CharField(max_length=100, null=True)),
                ('Zip2', models.CharField(max_length=100, null=True)),
                ('Addharcard_Number', models.CharField(max_length=100, null=True)),
                ('Addharcard_Picture', models.ImageField(null=True, upload_to='static')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SellerAccount')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_home.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='ecom_home.Address')),
                ('items', models.ManyToManyField(to='ecom_home.OrderItem')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='ecom_home.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item_by_seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_by_seller', models.CharField(max_length=100)),
                ('price_by_seller', models.FloatField()),
                ('discount_price_by_seller', models.FloatField(blank=True, null=True)),
                ('slug_by_seller', models.SlugField()),
                ('description_by_seller', models.TextField()),
                ('image_by_seller', models.ImageField(upload_to='static')),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.CATEGORY')),
                ('Sub_Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SUB_CATEGORY')),
                ('Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SUB_CATEGORY_Type')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SellerAccount')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='Sub_Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SUB_CATEGORY'),
        ),
        migrations.AddField(
            model_name='item',
            name='Type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SUB_CATEGORY_Type'),
        ),
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SellerAccount'),
        ),
        migrations.CreateModel(
            name='Display2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom_home.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_email', models.CharField(max_length=30)),
                ('user_phone_no', models.CharField(max_length=30, null=True)),
                ('user_address', models.CharField(max_length=300)),
                ('user_pincode', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
