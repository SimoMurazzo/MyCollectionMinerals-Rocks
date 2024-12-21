# Generated by Django 5.1.4 on 2024-12-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('locality', models.TextField()),
                ('mass_g', models.DecimalField(decimal_places=3, max_digits=10)),
                ('size_x_mm', models.PositiveIntegerField()),
                ('size_y_mm', models.PositiveIntegerField()),
                ('size_z_mm', models.PositiveIntegerField()),
                ('notes', models.TextField()),
                ('rarity', models.CharField(max_length=120)),
                ('formula', models.TextField()),
                ('environment', models.TextField()),
                ('crystal_system', models.CharField(max_length=120)),
                ('cleavage', models.CharField(max_length=120)),
                ('hardness', models.DecimalField(decimal_places=3, max_digits=5)),
                ('luminescence', models.CharField(max_length=120)),
                ('diaphaneity', models.CharField(max_length=120)),
                ('streak', models.CharField(max_length=120)),
                ('pleochroism', models.CharField(max_length=120)),
                ('radioactivity', models.CharField(max_length=120)),
                ('strunz_class', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
