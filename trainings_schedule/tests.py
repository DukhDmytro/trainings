from rest_framework import status
from rest_framework.test import APITestCase


class PostTestCase(APITestCase):

    def test_schedule_unauthorized(self):
        """Test unauthorised"""
        response = self.client.post('http://127.0.0.1:8000/schedule/', {}, HTTP_AUTHORIZATION='')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_schedule_one(self):
        """
        Schedule testing
        """
        # register user
        data = {'username': 'test_user', 'email': 'test@gmail.com', 'password': '12345'}
        response = self.client.post('http://127.0.0.1:8000/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # login user
        response = self.client.post('http://127.0.0.1:8000/login/', data)
        token = response.data['access']
        # try to create new training
        data = {'name': 'Python training', 'token': token}
        response = self.client.post('http://127.0.0.1:8000/schedule/',  data,
                                    HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # get list of trainings
        response = self.client.get('http://127.0.0.1:8000/schedule/', data,
                                    HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
