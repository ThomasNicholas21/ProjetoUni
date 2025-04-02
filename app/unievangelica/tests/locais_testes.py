from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from ..models import Bloco, RecursoSala, Sala, Cursos


class LocaisAPITestCase(APITestCase):
    def setUp(self):
        # Criar dados iniciais para os testes
        self.bloco1 = Bloco.objects.create(nome_bloco="Bloco A")
        self.bloco2 = Bloco.objects.create(nome_bloco="Bloco B")
        
        self.recurso1 = RecursoSala.objects.create(nome_recurso="Projetor")
        self.recurso2 = RecursoSala.objects.create(nome_recurso="Ar-condicionado")
        
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.curso = Cursos.objects.create(nome_curso="Engenharia de Software")
        self.curso.coordenador.add(self.user)
        
        self.sala_publica = Sala.objects.create(
            nome_sala="Sala 101",
            bloco=self.bloco1,
            quantidade_maxima=30,
            status="PUBLIC"
        )
        self.sala_publica.recursos_sala.add(self.recurso1)
        
        self.sala_privada = Sala.objects.create(
            nome_sala="Lab 201",
            bloco=self.bloco2,
            quantidade_maxima=20,
            status="PRIVATE",
            curso=self.curso
        )
        self.sala_privada.recursos_sala.add(self.recurso2)

    def test_get_blocos(self):
        url = reverse('api_get_blocos')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['nome_bloco'], "Bloco A")
        self.assertEqual(response.data[1]['nome_bloco'], "Bloco B")

    def test_post_bloco(self):
        url = reverse('api_post_bloco')
        data = {'nome_bloco': 'Bloco C'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bloco.objects.count(), 3)
        self.assertEqual(Bloco.objects.last().nome_bloco, 'Bloco C')

    def test_get_recursos_sala(self):
        url = reverse('api_get_recursos_sala')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['nome_recurso'], "Projetor")
        self.assertEqual(response.data[1]['nome_recurso'], "Ar-condicionado")

    def test_post_recurso_sala(self):
        url = reverse('api_post_recurso_sala')
        data = {'nome_recurso': 'Quadro branco'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RecursoSala.objects.count(), 3)
        self.assertEqual(RecursoSala.objects.last().nome_recurso, 'Quadro branco')

    def test_get_salas(self):
        url = reverse('api_get_salas')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['nome_sala'], "Sala 101")
        self.assertEqual(response.data[1]['nome_sala'], "Lab 201")

    def test_post_sala_publica(self):
        url = reverse('api_post_sala')
        data = {
            'nome_sala': 'Sala 102',
            'bloco': self.bloco1.id,
            'quantidade_maxima': 25,
            'status': 'PUBLIC',
            'recursos_sala': [self.recurso1.id],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sala.objects.count(), 3)
        self.assertEqual(Sala.objects.last().nome_sala, 'Sala 102')

    def test_post_sala_privada(self):
        url = reverse('api_post_sala')
        data = {
            'nome_sala': 'Lab 202',
            'bloco': self.bloco2.id,
            'quantidade_maxima': 15,
            'status': 'PRIVATE',
            'curso': self.curso.id,
            'recursos_sala': [self.recurso2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sala.objects.count(), 3)
        self.assertEqual(Sala.objects.last().nome_sala, 'Lab 202')

    def test_post_sala_privada_sem_curso_deve_falhar(self):
        url = reverse('api_post_sala')
        data = {
            'nome_sala': 'Lab 203',
            'bloco': self.bloco2.id,
            'quantidade_maxima': 15,
            'status': 'PRIVATE',
            'recursos_sala': [self.recurso2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Uma sala privada deve estar associada a um curso', str(response.data))

    def test_post_sala_com_capacidade_invalida_deve_falhar(self):
        url = reverse('api_post_sala')
        data = {
            'nome_sala': 'Sala 103',
            'bloco': self.bloco1.id,
            'quantidade_maxima': 0,
            'status': 'PUBLIC',
            'recursos_sala': [self.recurso1.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('Sala deve ter ao menos 1 de capacidade máxima', str(response.data))
