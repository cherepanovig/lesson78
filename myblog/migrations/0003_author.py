# Generated by Django 5.1.2 on 2024-10-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
            ],
        ),
    ]
