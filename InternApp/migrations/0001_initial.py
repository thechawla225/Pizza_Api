# Generated by Django 3.0.5 on 2021-05-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=100)),
                ('toppings', models.CharField(max_length=500)),
            ],
        ),
    ]