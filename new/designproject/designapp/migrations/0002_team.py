# Generated by Django 5.0.1 on 2024-01-17 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='designapp/team')),
            ],
        ),
    ]
