# Generated by Django 5.1.2 on 2024-10-09 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190122_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAuthentication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credentials', models.JSONField()),
                ('token', models.JSONField(null=True)),
            ],
        ),
    ]
