# Generated by Django 2.0.2 on 2018-04-07 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='sheet_name',
            field=models.CharField(max_length=150),
        ),
    ]
