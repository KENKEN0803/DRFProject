# Generated by Django 4.0.5 on 2022-06-18 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=140, null=True)),
                ('password', models.CharField(max_length=1000)),
                ('contents', models.TextField(null=True)),
                ('completed', models.BooleanField(default=False)),
                ('writtenTime', models.TimeField(default='00:00:00')),
            ],
        ),
    ]
