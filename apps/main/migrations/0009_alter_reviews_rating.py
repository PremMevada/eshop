# Generated by Django 3.2 on 2021-05-18 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='rating',
            field=models.IntegerField(max_length=100, null=True),
        ),
    ]
