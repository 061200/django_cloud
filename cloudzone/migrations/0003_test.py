# Generated by Django 4.0.4 on 2022-06-05 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloudzone', '0002_nonsmokingarea_smokingarea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
