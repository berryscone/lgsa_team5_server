# Generated by Django 4.0.5 on 2022-07-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('plate_number', models.CharField(db_index=True, default='', max_length=10)),
                ('status', models.CharField(default='', max_length=50)),
                ('reg_exp', models.CharField(default='', max_length=50)),
                ('owner', models.CharField(default='', max_length=50)),
                ('birth', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=100)),
                ('year', models.CharField(default='', max_length=50)),
                ('make', models.CharField(default='', max_length=50)),
                ('model', models.CharField(default='', max_length=50)),
                ('color', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
