# Generated by Django 4.1.13 on 2024-07-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_myuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
            ],
        ),
    ]
