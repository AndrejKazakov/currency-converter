# Generated by Django 4.2 on 2023-05-02 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Валюта',
                     'verbose_name_plural': 'Валюты'},
        ),
    ]