# Generated by Django 4.2.20 on 2025-04-01 15:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('unievangelica', '0007_sala_curso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='curso',
            field=models.ForeignKey(blank=True, help_text='Opcional, caso a sala seja pública.', null=True, on_delete=django.db.models.deletion.PROTECT, to='unievangelica.cursos', verbose_name='Curso associado:'),
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_final', models.DateTimeField()),
                ('motivo_reserva', models.TextField()),
                ('recorrencia', models.CharField(choices=[('NENHUMA', 'Nenhuma recorrência'), ('DIARIA', 'Diária'), ('SEMANAL', 'Semanal'), ('MENSAL', 'Mensal')], default='NENHUMA', max_length=10, verbose_name='Tipo de recorrência')),
                ('recorrencia_fim', models.DateTimeField(blank=True, null=True, verbose_name='Data final da recorrência')),
                ('dias_recorrencia', models.CharField(blank=True, help_text='Para recorrência semanal, informe os dias (ex: 2,4 para terça e quinta)', max_length=20, null=True)),
                ('bloco', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unievangelica.bloco')),
                ('coordenador', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='unievangelica.cursos')),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='unievangelica.sala')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
                'ordering': ['data_inicio'],
            },
        ),
    ]
