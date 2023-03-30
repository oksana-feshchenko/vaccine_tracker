from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tracker.models import Child, Vaccination, Complication, Vaccine


class PublicViewTest(TestCase):
    def test_login_not_required_index(self):
        result = self.client.get(reverse("tracker:index"))
        self.assertEqual(result.status_code, 200)

    def test_login_required_children_list_view(self):
        result = self.client.get(reverse("tracker:child-list"))
        self.assertNotEqual(result.status_code, 200)

    def test_login_required_vaccine_list_view(self):
        result = self.client.get(reverse("tracker:vaccine-list"))
        self.assertNotEqual(result.status_code, 200)


class PrivateViewChildTest(TestCase):
    def setUp(self) -> None:
        user = get_user_model().objects.create_user(
            username="test",
            password="12345",
            first_name="first_test",
            last_name="last_test",
        )
        self.client.force_login(user=user)

    def test_retrieve_child_list(self):
        Child.objects.create(
            first_name="first_test",
            last_name="last_test",
            gender="male",
            birth_date="2023-01-01",
            parent_id=1
        )

        child_list = Child.objects.all()
        result = self.client.get(reverse("tracker:child-list"))
        self.assertEqual(
            list(result.context["child_list"]), list(child_list)
        )
        self.assertEqual(result.status_code, 200)
        self.assertTemplateUsed(result, "tracker/child_list.html")


class PrivateViewVaccinationTest(TestCase):
    def setUp(self) -> None:
        user = get_user_model().objects.create_user(
            username="test",
            password="12345",
            first_name="first_test",
            last_name="last_test",
        )
        self.client.force_login(user=user)

    def test_child_detail(self):
        Child.objects.create(
            first_name="first_test",
            last_name="last_test",
            gender="male",
            birth_date="2023-01-01",
            parent_id=1
        )
        result = self.client.get(reverse("tracker:child-detail", args=["1"]))
        self.assertEqual(result.status_code, 200)


class PrivateViewComplicationTest(TestCase):
    def setUp(self) -> None:
        user = get_user_model().objects.create_user(
            username="test",
            password="12345",
            first_name="first_test",
            last_name="last_test",
        )
        self.client.force_login(user=user)

    def test_retrieve_complication_list(self):
        child=Child.objects.create(
            first_name="first_test",
            last_name="last_test",
            gender="male",
            birth_date="2023-01-01",
            parent_id=1
        )
        vaccine = Vaccine.objects.create(name="a",number_of_doses=0,age_for_first_dose_days=1)
        vaccination = Vaccination.objects.create(vaccine=vaccine, child=child)
        Complication.objects.create(description="asd",vaccination=vaccination)
        result = self.client.get(reverse("tracker:complication-list"))
        complications = Complication.objects.all()
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            list(result.context["complication_list"]), list(complications)
        )


