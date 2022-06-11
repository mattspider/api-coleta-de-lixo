# Generated by Django 4.0.3 on 2022-06-08 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anuncios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=255)),
                ('numero', models.CharField(default=0, max_length=255, null=True)),
                ('logradouro', models.CharField(max_length=255)),
                ('nome_da_rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('tipo', models.CharField(blank=True, max_length=255, null=True)),
                ('desc', models.CharField(blank=True, max_length=255, null=True)),
                ('seg', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Anuncio',
            },
        ),
        migrations.CreateModel(
            name='Infanunciante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=0, max_length=55, null=True)),
                ('cpf', models.CharField(default=0, max_length=55, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Infanunciante',
            },
        ),
        migrations.CreateModel(
            name='Infempresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, null=True)),
                ('cnpj', models.CharField(default=0, max_length=18, null=True)),
                ('rua', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('cidade', models.CharField(max_length=255)),
                ('numero', models.CharField(default=0, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Infempresa',
            },
        ),
    ]