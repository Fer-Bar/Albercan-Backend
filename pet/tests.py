from django.test import TestCase

from pet.models import Pet


class TestPet(TestCase):
    def test_create_pet_with_valid_instance(self):
        pet = Pet.objects.create(name="Peter")
        self.assertIsInstance(pet, Pet)
