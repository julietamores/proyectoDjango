# Generated by Django 3.2 on 2022-12-29 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oficina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre de la habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres')),
                ('dni', models.CharField(max_length=50, verbose_name='Dni')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oficina.oficina')),
                ('habilidades', models.ManyToManyField(to='empleado.Habilidad')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
            },
        ),
    ]