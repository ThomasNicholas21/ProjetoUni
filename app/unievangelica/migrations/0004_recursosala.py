# Generated by Django 4.2.20 on 2025-03-30 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unievangelica', '0003_alter_bloco_options_alter_sala_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoSala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_recurso', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Recurso da Sala',
                'verbose_name_plural': 'Recursos da Sala',
            },
        ),
    ]
