# Generated by Django 5.1.2 on 2024-10-19 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=67)),
                ('passwd', models.CharField(max_length=128)),
            ],
        ),
    ]
