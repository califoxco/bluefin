# Generated by Django 3.2.4 on 2021-06-22 08:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propertyID', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('slug', models.SlugField(default='0')),
                ('listed_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]