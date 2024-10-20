# Generated by Django 5.1.2 on 2024-10-20 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_usuario_created_at_remove_usuario_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('categoria', models.CharField(max_length=64)),
                ('info', models.CharField(max_length=128)),
                ('precio', models.FloatField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
            ],
        ),
        migrations.DeleteModel(
            name='usuario',
        ),
    ]
