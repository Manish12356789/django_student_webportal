# Generated by Django 4.0.6 on 2022-07-18 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_fname', models.CharField(max_length=255)),
                ('s_lname', models.CharField(max_length=255)),
                ('s_gender', models.CharField(max_length=255)),
                ('s_email', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]