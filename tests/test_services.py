from django.test import TestCase
from images.models import Image
from users.models import User
from .utils import create_image, update_image, delete_image


class ImageCreateTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test User')

    def test_creating_image(self):
        self.assertEqual(0, Image.objects.count())
        created_image = create_image(name='test', url='https://i.redd.it/jeuusd992wd41.jpg',
                                     slug='ta-ta-ta', owner=self.user, description='random pic')
        self.assertEqual(1, Image.objects.count())
        self.assertEqual(created_image, Image.objects.first())


class ImageUpdateTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test User')
        self.image1 = Image.objects.create(name='test', url='https://i.redd.it/jeuusd992wd41.jpg',
                                     slug='ta-ta-ta', owner=self.user, description='random pic')

    def test_creating_image(self):
        self.assertEqual(1, Image.objects.count())
        data = {
            'name': "really new name",
            'url': 'https://cs.pikabu.ru/post_img/big/2013/12/31/9/1388645055_1336973337.jpg',
            'slug': 'new-slug',
        }
        updated_image = update_image(self.image1, data)
        self.assertEqual(1, Image.objects.count())
        self.assertEqual(updated_image, Image.objects.first())
        self.assertEqual('new-slug', self.image1.slug)
        self.assertEqual('https://cs.pikabu.ru/post_img/big/2013/12/31/9/1388645055_1336973337.jpg', self.image1.url)
        self.assertEqual('really new name', self.image1.name)


class ImageDeleteTest(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='Test User')
        self.image1 = Image.objects.create(name='test', url='https://i.redd.it/jeuusd992wd41.jpg',
                                     slug='ta-ta-ta', owner=self.user, description='random pic')

    def test_delete_image(self):
        self.assertEqual(1, Image.objects.count())
        delete_image(self.image1)
        self.assertEqual(0, Image.objects.count())

