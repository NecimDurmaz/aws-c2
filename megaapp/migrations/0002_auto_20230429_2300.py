# Generated by Django 3.2.9 on 2023-04-29 23:00

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('megaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlassBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='glasscategory',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='glass',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='glasscategory',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AddField(
            model_name='glass',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='megaapp.glassbrand'),
        ),
    ]
