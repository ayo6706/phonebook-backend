# Generated by Django 3.1.4 on 2021-11-03 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20211022_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_picture',
            field=models.ImageField(null=True, upload_to='post_images'),
        ),
    ]
