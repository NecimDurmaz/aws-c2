# Generated by Django 3.2.9 on 2023-04-30 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('megaapp', '0002_auto_20230429_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='glass',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
