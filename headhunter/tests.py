from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Resume, ResumeStatus


class TestListUpdateResume(APITestCase):
    def setUp(self) -> None:
        self.test_user = User.objects.create_user(username='test_user')
        self.test_user2 = User.objects.create_user(username='test_user2')
        self.test_resume = Resume.objects.create(
            user=self.test_user,
            grade=ResumeStatus.PUBLISHED,
            specialty='backend_dev',
            title='ResumeTest',
            email='test@mail.ru'
        )

    def test_list_resumes(self):
        url = reverse('resume')
        self.client.force_authenticate(self.test_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_resume(self):
        url = reverse('resume_update', kwargs={'pk': self.test_resume.id})
        update_data = {
            'specialty': 'frontend_dev',
            'title': 'new_name',
            'email': 'strange@mail.ru',
        }
        self.client.force_authenticate(self.test_user)
        response = self.client.patch(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['specialty'], update_data['specialty'])

    def test_cannot_update_resume(self):
        url = reverse('resume_update', kwargs={'pk': self.test_resume.id})
        update_data = {
            'specialty': 'frontend_dev',
            'title': 'new_name',
            'email': 'strange@mail.ru',
        }
        self.client.force_authenticate(self.test_user2)
        response = self.client.patch(url, update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
