# Generated by Django 3.1.7 on 2021-03-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
