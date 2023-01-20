from django.db import models
from session.models import Session
# Create your models here.
class ClassCategory(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="title"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        primary_key=True,
        verbose_name="slug"
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Class category"
        verbose_name_plural = "Class categories"

class Class(models.Model):
    title = models.CharField(
        max_length=100,
        blank=False,
        verbose_name="title"
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name="classes",
        verbose_name="session"
    )
    class_category = models.ForeignKey(
        ClassCategory,
        on_delete=models.CASCADE,
        related_name="classes",
        verbose_name="class category"
    )

    def __str__(self):
        return f"{self.title}-{self.class_category}"

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

