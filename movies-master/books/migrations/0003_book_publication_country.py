# Generated by Django 5.0.6 on 2024-07-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_iban'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publication_country',
            field=models.CharField(default='Polska', max_length=255),
        ),
    ]
