from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Cursos, Reservas, Bloco, Sala, RecursoSala
from datetime import date, timedelta, time
import json

class ReservasAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='coordenador',
            password='testpass',
            first_name='João'
        )
        self.bloco = Bloco.objects.create(nome_bloco="Bloco Central")
        self.recurso = RecursoSala.objects.create(nome_recurso="Projetor")
        self.sala = Sala.objects.create(
            nome_sala="Sala 101",
            bloco=self.bloco,
            quantidade_maxima=30,
            status="PUBLIC"
        )
        self.sala.recursos_sala.add(self.recurso)
        self.curso = Cursos.objects.create(nome_curso="Engenharia de Software")
        self.curso.coordenador.add(self.user)
        self.amanha = date.today() + timedelta(days=1)
        self.reserva = Reservas.objects.create(
            nome_reserva="Aula de Programação",
            bloco=self.bloco,
            sala=self.sala,
            data_reserva=self.amanha,
            horario_inicio=time(14, 0),
            horario_final=time(16, 0),
            coordenador=self.user,
            motivo_reserva="Aula regular da disciplina",
            curso=self.curso
        )

    def test_get_reservas(self):
        url = reverse('api_get_reservas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome_reserva'], "Aula de Programação")

    def test_post_reserva(self):
        url = reverse('api_post_reservas')
        data = {
            'nome_reserva': 'Reunião de Planejamento',
            'bloco': self.bloco.id,
            'sala': self.sala.id,
            'data_reserva': str(self.amanha),
            'horario_inicio': '10:00:00',
            'horario_final': '12:00:00',
            'coordenador': self.user.id,
            'motivo_reserva': 'Reunião mensal de planejamento',
            'curso': self.curso.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservas.objects.count(), 2)
        self.assertEqual(Reservas.objects.last().nome_reserva, 'Reunião de Planejamento')

    def test_get_reserva_detail(self):
        url = reverse('api_get_reserva_detail', args=[self.reserva.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome_reserva'], "Aula de Programação")
        self.assertEqual(response.data['motivo_reserva'], "Aula regular da disciplina")

    def test_delete_reserva(self):
        url = reverse('api_delete_reserva_detail', args=[self.reserva.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Reservas.objects.count(), 0)

    def test_post_reserva_sem_dados_obrigatorios(self):
        url = reverse('api_post_reservas')
        data = {
            'nome_reserva': 'Reserva Inválida',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('bloco', response.data)
        self.assertIn('sala', response.data)
        self.assertIn('data_reserva', response.data)

    def test_post_reserva_com_horario_invalido(self):
        url = reverse('api_post_reservas')
        data = {
            'nome_reserva': 'Reserva Horário Inválido',
            'bloco': self.bloco.id,
            'sala': self.sala.id,
            'data_reserva': str(self.amanha),
            'horario_inicio': '16:00:00',
            'horario_final': '14:00:00',
            'coordenador': self.user.id,
            'motivo_reserva': 'Reserva com horário inválido',
            'curso': self.curso.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['non_field_errors'][0], 'O horário inicial não deve ser maior que o final.')

    def test_post_reserva_com_recorrencia(self):
        url = reverse('api_post_reservas')
        data = {
            'nome_reserva': 'Reunião Semanal',
            'bloco': self.bloco.id,
            'sala': self.sala.id,
            'data_reserva': str(self.amanha),
            'horario_inicio': '10:00:00',
            'horario_final': '12:00:00',
            'coordenador': self.user.id,
            'motivo_reserva': 'Reunião semanal da equipe',
            'curso': self.curso.id,
            'recorrencia': 'S', 
            'quantidade_recorrencia': 4 
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Reservas.objects.count(), 5) 

    def test_get_relatorio(self):
        url = reverse('api_reserva_disponivel')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
