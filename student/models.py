from django.db import models
from student_class.models import Class
from session.models import Session
class Student(models.Model):
    GENDER_CHOICES = (("male", "male"), ("female", "female"))
    STATUS_CHOICES = (("graduated", "graduated"),
                      ("out of", "out of"),
                      ("not confirmed", "not confirmed"),
                      ("active", "active"),
                      ("pre-registered", "pre-registered"))
    student_id = models.CharField(
        max_length=30,
        verbose_name="student's id"
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
    gender = models.CharField(
        max_length=50,
        choices=GENDER_CHOICES,
        blank=False,
        verbose_name="gender"
    )
    photo = models.ImageField(
        upload_to='media/student_images',
        blank=True, null=True,
        verbose_name="photo"
    )
    group = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name='students',
        verbose_name="class"
    )
    birthday = models.DateField(verbose_name="date of birth")
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        verbose_name="status"
    )
    admission_year = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name="students",
        verbose_name="admission year"
    )

    def create_student_id(self):
        import datetime
        today = datetime.date.today()
        year = today.year
        year = str(year)[2::]
        class_title = self.group.class_category.title
        if class_title in ["русский", "нулевой", "russian", "nulevoy"]:
            lang = "2"
        elif class_title in ["кыргызский", "kyrgyz"]:
            lang = "1"
        else:
            lang = "0"
        pk = str(self.pk)
        if len(pk) == 1:
            pk = "00" + pk
        elif len(pk) == 2:
            pk = "0" + pk
        student_id = "62" + str(year) + lang + pk
        self.student_id = student_id
        self.save()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class FamilyMember(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="family_members",
        verbose_name="student"
    )
    fullname = models.TextField(
        blank=False,
        null=False,
        verbose_name="full name"
    )
    who = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name="who"
    )
    address = models.TextField(
        blank=False,
        null=False,
        verbose_name="address"
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name="phone number"
    )
    id_passport = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="id passport"
    )
    work_place = models.TextField(
        null=True,
        blank=True,
        verbose_name="work place"
    )
    is_responsible = models.BooleanField(
        default=True,
        verbose_name="is responsible"
    )

    def __str__(self):
        return f"{self.who}-{self.fullname}"


    class Meta:
        verbose_name = "Family member"
        verbose_name_plural = "Family members"

