# Generated by Django 5.0.4 on 2024-07-07 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiai', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pesanan',
            old_name='item',
            new_name='items',
        ),
    ]