# Generated by Django 5.0.6 on 2024-07-06 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='iban',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
