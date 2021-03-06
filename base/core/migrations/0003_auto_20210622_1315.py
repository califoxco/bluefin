# Generated by Django 3.2.4 on 2021-06-22 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='propertyID',
            new_name='property_id',
        ),
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
        migrations.AddField(
            model_name='owner',
            name='email',
            field=models.EmailField(default=0, max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='first_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='last_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='phone',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='owner',
            name='status',
            field=models.CharField(default='Active', max_length=100),
        ),
        migrations.AddField(
            model_name='property',
            name='address_1',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='address_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.CharField(default='Beautiful country home', max_length=500),
        ),
        migrations.AddField(
            model_name='property',
            name='number_baths',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='number_bedroom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='square_feet',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='state',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property',
            name='zip',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
