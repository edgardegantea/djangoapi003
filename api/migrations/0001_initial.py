# Generated by Django 4.1.2 on 2022-10-13 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Autor')),
                ('nacionalidad', models.CharField(choices=[('Mexicana', 'Mexicana'), ('Inglesa', 'Inglesa'), ('Española', 'Española')], default='Mexicana', max_length=30, verbose_name='Nacionalidad')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Título')),
                ('Autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.autor', verbose_name='Seleccione autor')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
    ]
