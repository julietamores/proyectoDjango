# Generated by Django 3.2 on 2023-01-04 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0003_alter_empleado_nombre_completo'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='empleado', verbose_name='imagen'),
        ),
    ]
