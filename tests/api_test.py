from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from images.models import Image
from users.models import User


class TestCurrentUser(APITestCase):
    def setUp(self) -> None:
        self.username = 'Tester1'
        self.password = '12345bestpassword'
        self.data = {
            'username': self.username,
            'password': self.password,
        }
        url = reverse('token_obtain_pair')
        self.user1 = User.objects.create(username=self.username, password=self.password)
        self.user1.set_password(self.password)
        self.user1.save()
        self.assertEqual(self.user1.is_active, 1, 'Active User')

        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_current_user(self):

        response = self.client.get(reverse('users-profile'), data={'format': 'json'})
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)


    def test_delete_image_owner(self):
        self.image1 = Image.objects.create(
            name='test1',
            url='https://cs.pikabu.ru/post_img/big/2013/12/31/9/1388645055_1336973337.jpg',
            slug='test',
            owner=self.user1
        )

        url = reverse('delete-image', args=(self.image1.slug, ))
        response = self.client.delete(url, format='json')

        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)
        self.assertEqual(0, Image.objects.count())


class TestUserPermissions(APITestCase):
    def setUp(self) -> None:
        self.user1 = User.objects.create(username='Test user1')
        self.image1 = Image.objects.create(owner=self.user1,
                                           name='test1',
                                           url='https://cs.pikabu.ru/post_img/big/2013/12/31/9/1388645055_1336973337.jpg',
                                           slug='test-slug')

    def test_delete_image_not_owner(self):

        """second user registers"""
        data = {
                'username': 'Tester2',
                'password': '123454321'
        }

        self.user2 = User.objects.create(username=data['username'], password=data['password'])
        self.user2.set_password(data['password'])
        self.user2.save()
        self.assertEqual(self.user2.is_active, 1, 'Active User')

        """second user obtains token"""
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.content)
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        """second tries to delete user's1 image"""
        url = reverse('delete-image', args=(self.image1.slug, ))
        response = self.client.delete(url)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(1, Image.objects.count())
