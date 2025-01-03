# Generated by Django 5.1.4 on 2024-12-27 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Minerals', '0003_rename_diaphaneity_mineral_luster_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mineral',
            name='cleavage',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='crystal_system',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='formula',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='hardness',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='luster',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='streak',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='mineral',
            name='strunz_class',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
