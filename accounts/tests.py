from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
#from accounts.urls import urlpatterns
from .models import UserData
from annoucement.models import Annoucement , Annoucement_category

# Create your tests here.
class TestAccounts(APITestCase):

    def setUp(self):
        self.user1 = UserData.objects.create(name = 'adam', email = 'adam@email.com', password = 'admin', is_active = 'True')
        self.ann_cat1 = Annoucement_category.objects.create(category_name='Auto')
        self.ann1 = Annoucement.objects.create(user =self.user1, title = 'test!!!!',
                                                        description = "test in rest",
                                                        category_name=self.ann_cat1,
                                                        annoucement_status = 'accepted')

    def authenticate(self):
        self.client.post(reverse('sign_up'),{ "email": "jan@email.com","name": "jan", "password": "admin"}, format = 'json')
        responce = self.client.post(reverse('token_obtain_pair'), {"email": "jan@email.com", "password": "admin"}, format = 'json')
        #token = Token.objects.get(user__name=self.clark_user.username)

        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {responce.data['access']}")
        # self.ann1 = Annoucement.objects.create(user=, title='test!!!!',
        #                                        description="test in rest",
        #                                        category_name=self.ann_cat1,
        #                                        annoucement_status='accepted')

    def test_register_user(self):
        responce = self.client.post(reverse('sign_up'), {"email": "jan@email.com", "name": "jan", "password": "admin"},
                         format='json')
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        self.client.post(reverse('sign_up'),{ "email": "jan@email.com","name": "jan", "password": "admin"}, format = 'json')
        responce = self.client.post(reverse('token_obtain_pair'), {"email": "jan@email.com", "password": "admin"}, format = 'json')
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_user_deatail(self):
        responce = self.client.get(reverse('profile_detail', kwargs={"pk": self.user1.id}))
        print(f"user_detail:{responce.data}")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


    def test_user_annoucements_list(self):
        self.authenticate()
        responce = self.client.get(reverse('profile_annoucements'))
        print(f"ann_list:{responce.data}")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)


