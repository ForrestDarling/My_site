# Generated by Django 4.1.6 on 2023-02-18 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, default='')),
                ('image', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('excerpt', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
    ]
