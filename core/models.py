from django.db import models
from shortuuid.django_fields import ShortUUIDField
import shortuuid
import string


def generate_short_uuid():
    return shortuuid.ShortUUID(alphabet=string.ascii_letters + string.digits).random(length=10)


class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)
    unit_id = ShortUUIDField(
        unique=True,
        length=10,
        max_length=20,
        alphabet=string.ascii_letters + string.digits,
        default=generate_short_uuid,
        null=True,  # Add this temporarily
        blank=True  # Add this temporarily
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    surname = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    other_names = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    command = models.CharField(max_length=100, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='employees')
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    next_of_kin_name = models.CharField(max_length=100, blank=True, null=True)
    next_of_kin_phone = models.CharField(max_length=100, blank=True, null=True)

    post = models.CharField(max_length=100, blank=True, null=True)
    pin = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    employee_id = ShortUUIDField(
        unique=True,
        length=10,
        max_length=20,
        alphabet=string.ascii_letters + string.digits,
        default=generate_short_uuid,
        null=True,  # Add this temporarily
        blank=True  # Add this temporarily
    )

    def __str__(self):
        return f"{self.name} ({self.unit.name})"
