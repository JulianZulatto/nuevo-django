# Generated by Django 4.2.6 on 2023-11-04 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('automovil', '0002_rename_auto_automovil'),
    ]

    operations = [
        migrations.AddField(
            model_name='automovil',
            name='descripcion',
            field=models.CharField(default='descripcion', max_length=250),
            preserve_default=False,
        ),
    ]
