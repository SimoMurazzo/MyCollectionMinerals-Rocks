# Generated by Django 5.1.4 on 2024-12-26 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minerals', '0002_alter_mineral_locality_alter_mineral_mass_g_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mineral',
            old_name='diaphaneity',
            new_name='luster',
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luminescence',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='pleochroism',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='radioactivity',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='rarity',
            field=models.CharField(max_length=120),
        ),
    ]
