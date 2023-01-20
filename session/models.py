from django.db import models

class Session(models.Model):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        primary_key=True,
        verbose_name="slug"
    )
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="title"
    )

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"



