# Generated by Django 4.2.4 on 2023-08-05 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processos', '0006_controlador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controlador',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
