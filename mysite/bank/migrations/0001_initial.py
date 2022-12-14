# Generated by Django 4.1.3 on 2022-11-24 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=255)),
                ('phone_number', models.IntegerField()),
                ('card_number', models.BigIntegerField(unique=True)),
                ('mail', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('amount_of_funds', models.IntegerField(default=0)),
            ],
        ),
    ]
