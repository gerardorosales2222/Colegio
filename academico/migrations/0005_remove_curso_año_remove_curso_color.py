# Generated by Django 5.0 on 2024-08-27 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academico', '0004_remove_profesor_titulo_profesor_titulos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='año',
        ),
        migrations.RemoveField(
            model_name='curso',
            name='color',
        ),
    ]
