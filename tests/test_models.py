from django.contrib.auth import get_user_model
from django.test import TestCase

from tracker.models import Child, Vaccine, Vaccination


class ModelTest(TestCase):
    def test_model_child_str(self):
        get_user_model().objects.create_user(
            username="test",
            password="12345",
            first_name="first_test",
            last_name="last_test",
        )
        child = Child.objects.create(
            first_name="first_test",
            last_name="last_test",
            gender="male",
            birth_date="2023-01-01",
            parent_id=1,
        )
        self.assertEqual(str(child), f"{child.first_name} {child.last_name}")

    def test_model_vaccine_str(self):
        vaccine = Vaccine.objects.create(
            name="a", number_of_doses=0, age_for_first_dose_days=1
        )

        self.assertEqual(str(vaccine), vaccine.name)

    def test_model_vaccination_str(self):
        get_user_model().objects.create_user(
            username="test",
            password="12345",
            first_name="first_test",
            last_name="last_test",
        )
        child = Child.objects.create(
            first_name="first_test",
            last_name="last_test",
            gender="male",
            birth_date="2023-01-01",
            parent_id=1,
        )
        vaccine = Vaccine.objects.create(
            name="a", number_of_doses=0, age_for_first_dose_days=1
        )
        vaccination = Vaccination.objects.create(vaccine=vaccine, child=child)
        self.assertEqual(
            str(vaccination),
            f"{vaccination.vaccine} for {vaccination.child}",
        )
