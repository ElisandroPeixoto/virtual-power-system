# Generated by Django 4.0.4 on 2022-05-31 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Membro da Equipe'),
        ),
    ]
