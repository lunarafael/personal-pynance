# Generated by Django 5.2 on 2025-04-16 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_remove_category_nome_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
