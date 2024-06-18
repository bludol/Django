# Generated by Django 5.0.6 on 2024-06-17 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RFPapp', '0003_kapela_obrazek'),
    ]

    operations = [
        migrations.AddField(
            model_name='kapela',
            name='popis',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='kapela',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='osoba',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pisnicka',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
