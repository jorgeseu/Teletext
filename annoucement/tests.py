from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
#from accounts.urls import urlpatterns
from accounts.models import UserData
from .models import Annoucement_category ,Annoucement

# Create your tests here.
class TestAnnoucementList(APITestCase):

    def setUp(self):
        self.user1 = UserData.objects.create(name='adam', email='adam@email.com', password='admin', is_active='True')
       # self.user2 = UserData.objects.create(name='jan', email='jan@email.com', password='admin', is_active='True')
        self.ann_cat1 = Annoucement_category.objects.create(category_name ='Auto')
        self.ann1 = Annoucement.objects.create(user=self.user1, title='test!!!!',
                                               description="test in rest",
                                               category_name=self.ann_cat1,
                                               annoucement_status='accepted')

    def authenticate(self):
        self.client.post(reverse('sign_up'), { "email": "jan@email.com","name": "jan", "password": "admin"}, format = 'json')
        responce = self.client.post(reverse('token_obtain_pair'), {"email": "jan@email.com", "password": "admin"}, format = 'json')
        #token = Token.objects.get(user__name=self.clark_user.username)
        self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {responce.data['access']}")

    def create_annoucement(self):
        self.authenticate()
        sample_ann = {"title": "test", "description": "test sample", "category_name": self.ann_cat1.id,
                      "annoucement_status": "accepted"}
        responce = self.client.post(reverse('annoucement_list_all'), sample_ann)
        return responce

    def get_annouceemnt(self):
        responce = self.client.get(reverse('annoucement_list_all'), )
        return responce

    # def login(self):
    #     user = self.user1
    #     responce = self.client.post(reverse('token_obtain_pair'), {"email": user.email, "password": user.password},
    #                                 format='json')
    #     self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {responce.data['access']}")

    def test_create_annoucement_no_auth(self):
        sample_ann = { "title": "enpointy ","description": "opel astra ", "category_name": self.ann_cat1.id, "annoucement_status": "accepted"}
        responce = self.client.post(reverse('annoucement_list_all'), sample_ann)

        self.assertEqual(responce.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_annoucement_with_auth(self):
        previous_ann_count = Annoucement.objects.all().count()
        self.authenticate()
        #user = Userdata.objects.get(name='ala')
        #self.client.force_authenticate(user=None)
        sample_ann = {"title": "enpointy", "description": "opel astra", "category_name": self.ann_cat1.id, "annoucement_status": "accepted"}
        responce = self.client.post(reverse('annoucement_list_all'), sample_ann)

        print(f"ann_create :{responce.data}")
        self.assertEqual(responce.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Annoucement.objects.all().count(), previous_ann_count+1)
        self.assertEqual(responce.data['title'], 'enpointy')
        self.assertEqual(responce.data['category_name'], self.ann_cat1.id)

    def test_update_annoucement_with_no_owner_user(self):
        self.authenticate()
        annoucement = self.ann1
        id = annoucement.id

        annoucement = {"id": id,"title": "update test ", "description": "opel astraaaaaa ", "category_name": self.ann_cat1.id, "annoucement_status": "accepted"}
        print(f"ann_update_no_owner :{annoucement['id']}")
        responce = self.client.put(reverse('annoucement_update', kwargs={"pk": annoucement['id']}), annoucement)
        self.assertEqual(responce.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_annoucement_by_owner_hardcoded(self):
        self.authenticate()
        previous = self.create_annoucement()
        catch = self.get_annouceemnt()
       # print(f"ann_update_owner 1 :{catch.data[1]['id']}")

        annoucement = catch.data[1]
        id = annoucement['id']
        #print(f"ann_update_owner 1-1 :{annoucement['id']}")
        annoucement = { "id": id,"title": "update test ", "description": "opel astraaaaaa ",
                       "category_name": self.ann_cat1.id, "annoucement_status": "accepted"}

        responce = self.client.put(reverse('annoucement_update', kwargs={"pk": annoucement['id']}), annoucement)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)

    # def test_update_by_owner(self):
    #     self.login()
    #     catch = self.get_annouceemnt()
    #     annoucement = catch.data
    #     id = annoucement['id']
    #     #print(f"ann_update_owner 1-1 :{annoucement['id']}")
    #     annoucement = { "id": id,"title": "update test ", "description": "opel astraaaaaa ",
    #                    "category_name": self.ann_cat1.id, "annoucement_status": "accepted"}
    #
    #     responce = self.client.put(reverse('annoucement_update', kwargs={"pk": annoucement['id']}), annoucement)
    #     self.assertEqual(responce.status_code, status.HTTP_200_OK)

    def test_delete_annoucement_by_owner(self):
        self.authenticate()
        previous = self.create_annoucement()
        catch = self.get_annouceemnt()
        #print(f"ann_delete_owner 1 :{catch.data}")

        annoucement = catch.data[1]
        id = annoucement['id']
        #print(f"ann_delete_owner 1-1 :{annoucement['id']}")

        responce = self.client.delete(reverse('annoucement_update', kwargs={"pk": annoucement['id']}), annoucement)
        self.assertEqual(responce.status_code, status.HTTP_204_NO_CONTENT)


    def test_annoucements_list(self):
        self.authenticate()
        responce = self.client.get(reverse('annoucement_list_all'),)
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertIsInstance(responce.data, list)

        #add annoucement
        sample_ann = {"title": "enpointy", "description": "opel astra", "category_name": self.ann_cat1.id,
                      "annoucement_status": "accepted"}
        self.client.post(reverse('annoucement_list_all'), sample_ann)

        res = self.client.get(reverse('annoucement_list_all'))
        # if list are not empty return true
        self.assertTrue(res.data)

    def test_annoucements_list_by_category(self):
        self.authenticate()
        responce = self.client.get(reverse('annoucement_category'),)

        print(f"ann_category :{responce.data}")
        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertIsInstance(responce.data, list)
        self.assertTrue(responce.data)



