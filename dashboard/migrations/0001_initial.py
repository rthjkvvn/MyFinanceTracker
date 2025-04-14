# Generated by Django 5.2 on 2025-04-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
