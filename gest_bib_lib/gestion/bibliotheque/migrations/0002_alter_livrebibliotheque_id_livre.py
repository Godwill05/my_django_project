# Generated by Django 4.2.4 on 2024-02-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livrebibliotheque',
            name='id_livre',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
