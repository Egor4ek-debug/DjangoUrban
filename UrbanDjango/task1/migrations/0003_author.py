# Generated by Django 5.1.4 on 2024-12-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
