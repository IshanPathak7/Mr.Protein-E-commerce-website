# Generated by Django 3.1.5 on 2021-06-25 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_product_cs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category'),
        ),
    ]
