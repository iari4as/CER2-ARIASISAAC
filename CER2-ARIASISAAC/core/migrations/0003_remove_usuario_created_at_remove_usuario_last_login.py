# Generated by Django 5.1.2 on 2024-10-19 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_usuario_codigo_usuario_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='last_login',
        ),
    ]
