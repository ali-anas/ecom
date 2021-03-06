# Generated by Django 2.2.14 on 2020-11-29 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SHIPPING_MODE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Shipping_Mode', models.CharField(default=None, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='MRP',
            field=models.FloatField(default=10),
        ),
        migrations.AddField(
            model_name='item',
            name='Pincode_pro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Produt_tax_code',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Shipping_Mode',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom_home.SHIPPING_MODE'),
        ),
    ]
