# Generated by Django 5.0.4 on 2024-04-06 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Santexnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('target_product', models.CharField(max_length=100)),
                ('standard_installation_count', models.CharField(max_length=100)),
                ('years_of_working', models.CharField(max_length=100)),
            ],
        ),
    ]
