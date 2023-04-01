from django.contrib.auth.models import AbstractUser
from django.db import models

from vaccination_tracker import settings


class Parent(AbstractUser):
    pass


class Child(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    birth_date = models.DateField()
    parent = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        related_name="children",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "children"
        ordering = ["birth_date"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Vaccine(models.Model):
    name = models.CharField(max_length=50, unique=True)
    number_of_doses = models.IntegerField(default=1)
    age_for_first_dose_days = models.IntegerField(default=0)

    class Meta:
        ordering = ["age_for_first_dose_days"]

    def __str__(self):
        return self.name


class Vaccination(models.Model):
    vaccine = models.ForeignKey(
        to=Vaccine, related_name="vaccines", on_delete=models.CASCADE
    )
    child = models.ForeignKey(
        to=Child, on_delete=models.CASCADE, related_name="vaccinations"
    )
    date_vaccination = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ["date_vaccination"]

    def __str__(self):
        return f"{self.vaccine} for {self.child}"


class Complication(models.Model):
    description = models.CharField(max_length=50)
    date_occurrence = models.DateTimeField(auto_now_add=True)
    vaccination = models.ForeignKey(
        to=Vaccination, related_name="complications", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.description
