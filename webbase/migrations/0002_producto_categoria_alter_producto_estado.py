# Generated by Django 4.1.7 on 2023-02-27 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webbase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.IntegerField(),
        ),
    ]