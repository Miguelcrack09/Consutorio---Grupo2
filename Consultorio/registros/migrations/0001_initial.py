# Generated by Django 3.2.7 on 2021-10-11 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('apellido', models.CharField(blank=True, max_length=45, null=True)),
                ('cedula', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('genero', models.CharField(blank=True, max_length=45, null=True)),
                ('correo', models.EmailField(max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=45, null=True)),
                ('contraseña', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
    ]
