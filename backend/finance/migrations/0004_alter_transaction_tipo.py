# Generated by Django 5.2 on 2025-04-16 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='tipo',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10),
        ),
    ]
