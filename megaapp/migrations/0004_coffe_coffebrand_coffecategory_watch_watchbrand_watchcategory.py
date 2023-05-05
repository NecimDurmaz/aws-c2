# Generated by Django 3.2.9 on 2023-04-30 06:19

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('megaapp', '0003_glass_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='CoffeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='WatchBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='WatchCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('image', models.ImageField(upload_to='watch')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='megaapp.watchbrand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megaapp.watchcategory')),
            ],
        ),
        migrations.CreateModel(
            name='Coffe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
                ('image', models.ImageField(upload_to='coffe')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='megaapp.coffebrand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='megaapp.coffecategory')),
            ],
        ),
    ]
