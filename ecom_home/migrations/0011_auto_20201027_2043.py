# Generated by Django 2.2.14 on 2020-10-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0010_auto_20201027_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to='static'),
        ),
    ]