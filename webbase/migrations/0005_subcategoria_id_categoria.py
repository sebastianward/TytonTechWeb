# Generated by Django 4.1.7 on 2023-03-01 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbase', '0004_carro'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategoria',
            name='id_categoria',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
