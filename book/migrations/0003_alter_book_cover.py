# Generated by Django 4.0.4 on 2022-06-13 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='Default.jpg', upload_to='media'),
        ),
    ]
