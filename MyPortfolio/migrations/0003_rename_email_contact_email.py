# Generated by Django 5.0.3 on 2024-04-03 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolio', '0002_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
    ]