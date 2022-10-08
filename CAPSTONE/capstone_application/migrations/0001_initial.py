# Generated by Django 4.0.3 on 2022-10-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('breed', models.CharField(max_length=64)),
                ('age', models.CharField(max_length=64)),
                ('size', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='static/')),
                ('location', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=64)),
            ],
        ),
    ]
