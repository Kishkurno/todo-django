# Generated by Django 4.2.13 on 2024-06-13 20:27

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
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
