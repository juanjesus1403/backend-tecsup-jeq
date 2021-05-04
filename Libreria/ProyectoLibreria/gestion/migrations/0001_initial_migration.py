# Generated by Django 3.2 on 2021-05-04 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaModel',
            fields=[
                ('categoriaId', models.AutoField(db_column='id', primary_key=True, serialize=False, unique=True)),
                ('categoriaNombre', models.CharField(db_column='nombre', help_text='Nombre de la categoria', max_length=45, verbose_name='nombre')),
            ],
            options={
                'verbose_name': 'categoria',
                'verbose_name_plural': 'categorias',
                'db_table': 'categorias',
            },
        ),
    ]
