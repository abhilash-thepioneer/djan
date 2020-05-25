# Generated by Django 3.0.2 on 2020-04-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200402_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=111)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip_code', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
