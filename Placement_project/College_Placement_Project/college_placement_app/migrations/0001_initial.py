# Generated by Django 4.0.2 on 2022-02-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Image/')),
                ('name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('year', models.ImageField(upload_to='')),
                ('company', models.CharField(max_length=200)),
                ('package', models.ImageField(upload_to='')),
            ],
        ),
    ]
