# Generated by Django 3.2 on 2022-12-29 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='nombre_completo',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre completo'),
            preserve_default=False,
        ),
    ]