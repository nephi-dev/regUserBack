# Generated by Django 3.1.7 on 2021-03-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cep',
            field=models.IntegerField(null=True, verbose_name='cep'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=256, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=256, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.IntegerField(null=True, verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='houseNumber',
            field=models.PositiveIntegerField(null=True, verbose_name='houseNumber'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pis',
            field=models.IntegerField(null=True, verbose_name='pis'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=256, null=True, verbose_name='state'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='street',
            field=models.CharField(max_length=256, null=True, verbose_name='street'),
        ),
    ]
