# Generated by Django 2.2.6 on 2020-06-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_shelter', '0003_auto_20200630_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kind',
            name='name',
            field=models.CharField(choices=[('DOG', 'СОБАКА'), ('CAT', 'КОШКА'), ('PAR', 'ПОПУГАЙ')], default='DOG', max_length=3),
        ),
    ]