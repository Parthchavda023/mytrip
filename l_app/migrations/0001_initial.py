# Generated by Django 5.0.3 on 2024-03-15 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signupModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fnm', models.CharField(max_length=50)),
                ('lnm', models.CharField(max_length=50)),
                ('unm', models.EmailField(max_length=254)),
                ('pas', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('number', models.BigIntegerField()),
            ],
        ),
    ]