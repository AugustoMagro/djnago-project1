# Generated by Django 5.1 on 2024-08-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0004_photos_date_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
