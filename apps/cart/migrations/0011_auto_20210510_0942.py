# Generated by Django 3.2 on 2021-05-10 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_auto_20210510_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='rate',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='sales',
            name='subtotal',
            field=models.PositiveIntegerField(default=models.PositiveIntegerField(default=0)),
        ),
    ]
