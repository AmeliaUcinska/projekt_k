# Generated by Django 5.1.2 on 2025-01-20 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0010_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nazwa wycieczki')),
                ('description', models.TextField(verbose_name='Opis')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Cena')),
                ('available', models.BooleanField(default=True, verbose_name='Dostępność')),
            ],
        ),
    ]
