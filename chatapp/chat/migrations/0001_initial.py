# Generated by Django 4.1.1 on 2023-05-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=80)),
                ('response', models.TextField()),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]