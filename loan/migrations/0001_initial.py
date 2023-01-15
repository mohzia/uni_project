# Generated by Django 4.0.4 on 2022-05-30 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('C', 'Chosing'), ('S', 'Started'), ('R', 'Reterned'), ('T', 'To be reterned')], max_length=35)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.customuser')),
            ],
        ),
    ]
