# Generated by Django 2.2.14 on 2020-12-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0013_auto_20201205_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='apartment_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='landmark',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='street_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='zip_code',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
