# Generated by Django 2.2.14 on 2020-12-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_home', '0023_category_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(null=True, upload_to='')),
                ('color', models.CharField(default='#FFFFFF', max_length=30, null=True)),
            ],
        ),
    ]