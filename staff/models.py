from django.db import models
from django.contrib.auth import get_user_model
from student_class.models import Class

User = get_user_model()

class Nationality(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=150,
        verbose_name="slug"
    )
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name="title"
    )

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"


class Citizenship(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=150,
        verbose_name="slug"
    )
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name="title"
    )

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Citizenship"
        verbose_name_plural = "Citizenships"

class MaritalStatus(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=150,
        verbose_name="slug"
    )
    title = models.CharField(
        max_length=150,
        blank=False,
        null=False,
        verbose_name="title"
    )

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Marital status"
        verbose_name_plural = "Marital status"

class Specilaty(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=200,
        verbose_name="slug"
    )
    title = models.CharField(
        max_length=200,
        blank=False,
        null=False,
        verbose_name="title"
    )

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Specialty"
        verbose_name_plural = "Specialties"

class Staff(models.Model):
    GENDER = (("male", "male"), ("female", "female"))
    POSITION = (
        ("director", "director"),
        ("accountant", "accountant"),
        ("staff", "staff")
    )
    STATUS = (
        ("Уволен", "Уволен"),
        ("Работает", "Работает"),
        ("Перведен в другую школу", "Перведен в другую школу"),
        ("В декретном отпуске", "В декретном отпуске"),
        ("Перведен из другой школы", "УволПерведен из другой школыен")

    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="staff"
    )
    username = models.CharField(
        max_length=100,
        unique=True,
        blank=True,
        null=True,
        verbose_name="username"
    )
    password = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="password"
    )
    first_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="first name"
    )
    last_name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="last name"
    )
    patronymic = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="patronymic"
    )
    birthday = models.DateField(verbose_name="date")
    gender = models.CharField(
        choices=GENDER,
        max_length=10,
        blank=False,
        null=False,
        verbose_name="gender"
    )
    position = models.CharField(
        choices=POSITION,
        max_length=50,
        blank=False,
        null=False,
        verbose_name="specialty"
    )
    photo = models.ImageField(
        upload_to='media/student_images',
        blank=True,
        null=True,
        verbose_name="photo"
    )
    class_id = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="class",
        related_name="staffs"
    )
    status = models.CharField(
        choices=STATUS,
        max_length=100,
        blank=False,
        null=False,
        verbose_name="status"
    )
    nationality = models.ForeignKey(
        Nationality,
        on_delete=models.CASCADE,
        related_name="staff",
        verbose_name="nationality",
        blank=False,
        null=False
    )
    citizenship = models.ForeignKey(
        Citizenship,
        on_delete=models.CASCADE,
        related_name="staff",
        verbose_name="citizenship",
        blank=False,
        null=False
    )
    marital_status = models.ForeignKey(
        MaritalStatus,
        on_delete=models.CASCADE,
        related_name="staff",
        verbose_name="marital status",
        blank=False,
        null=False
    )
    specialty = models.ForeignKey(
        Specilaty,
        on_delete=models.CASCADE,
        related_name="staff",
        verbose_name="nationality",
        blank=False,
        null=False
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialty}"

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

class StaffContactInfo(models.Model):
    staff = models.OneToOneField(
        Staff,
        on_delete=models.CASCADE,
        related_name="staff_contact_info",
        blank=False,
        null=False,
        verbose_name="staff"
    )
    birthplace=models.TextField(
        blank=True,
        null=True,
        verbose_name="birthplace"
    )
    email = models.EmailField(
        blank=True,
        null=True,
        verbose_name="email"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=False,
        null=False,
        verbose_name="phone number"
    )
    id_passport = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="id passport"
    )
    issuing_authority = models.TextField(
        blank=True,
        null=True,
        verbose_name="issuing authority",
    )
    date_of_issue = models.DateField(
        blank=True,
        null=True,
        verbose_name="date of issue"
    )
    inn = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="inn"
    )
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.specialty}"

    class Meta:
        verbose_name = "Staff's contact information"
        verbose_name_plural = "Staff's contact informations"