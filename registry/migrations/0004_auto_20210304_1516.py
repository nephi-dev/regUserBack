# Generated by Django 3.1.7 on 2021-03-04 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_auto_20210304_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.IntegerField(blank=True, null=True, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='houseNumber',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='houseNumber'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pis',
            field=models.IntegerField(blank=True, null=True, verbose_name='pis'),
        ),
    ]