from datetime import timedelta

from django.test import Client, TestCase
from django.urls import reverse

from pet.models import Breed, Pet
from utils.datetools import utc_now


class MainPageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.first_breed = Breed.objects.create(name="Breed1")
        self.second_breed = Breed.objects.create(name="Breed2")
        self.first_pet = Pet.objects.create(
            name="Pet1",
            breed=self.first_breed,
            birthday=utc_now() - timedelta(days=365),
        )
        self.second_pet = Pet.objects.create(
            name="Pet2",
            breed=self.second_breed,
            birthday=utc_now() - timedelta(days=730),
        )

    def test_main_page_status_code(self):
        response = self.client.get(reverse("main_page"))
        self.assertEqual(response.status_code, 200)

    def test_main_page_template_used(self):
        response = self.client.get(reverse("main_page"))
        self.assertTemplateUsed(response, "pet/main_page.html")

    def test_main_page_contains_correct_html(self):
        response = self.client.get(reverse("main_page"))
        self.assertContains(response, "¡Haz un cambio hoy!")
        self.assertContains(response, "Pet1")
        self.assertContains(response, "Pet2")

    def test_main_page_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse("main_page"))
        self.assertNotContains(response, "Hello, world!")

    def test_main_page_context(self):
        response = self.client.get(reverse("main_page"))
        self.assertTrue("pets" in response.context)
        self.assertTrue("headlines" in response.context)
        self.assertEqual(len(response.context["pets"]), 2)
        self.assertEqual(
            set(response.context["pets"]), {self.first_pet, self.second_pet}
        )
