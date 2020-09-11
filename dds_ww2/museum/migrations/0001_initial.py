# Generated by Django 2.2.16 on 2020-09-09 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='battle',
            fields=[
                ('battle_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('battle_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ships',
            fields=[
                ('ship_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=100)),
                ('launched', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='outcomes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle_name', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=100)),
                ('ship_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museum.ships')),
            ],
        ),
    ]