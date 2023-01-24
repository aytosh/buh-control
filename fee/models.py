from django.db import models
from student.models import Student
from finance.models import Cashbox

class Discount(models.Model):
    title = models.TextField(
        blank=False,
        null=True,
        verbose_name="title"
    )
    amount_usd = models.FloatField(
        blank=False,
        null=False,
        verbose_name="amount usd"
    )

    def __str__(self):
        return f"{self.title}-{self.amount_usd}"

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"


class FeeCategory(models.Model):
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="title"
    )
    amount_usd = models.FloatField(
        blank=False,
        null=False,
        verbose_name="amount usd"
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="note"
    )

    def __str__(self):
        return f"{self.title}-{self.amount_usd}"

    class Meta:
        verbose_name = "Fee category"
        verbose_name_plural = "Fee categories"

class Fee(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="fees",
        verbose_name="student"
    )
    fee_category = models.ForeignKey(
        FeeCategory,
        on_delete=models.CASCADE,
        related_name="fees",
        verbose_name="fee category"
    )
    discount = models.ForeignKey(
        Discount,
        on_delete=models.CASCADE,
        related_name="fees",
        verbose_name="discount"
    )
    payment_usd = models.FloatField(
        verbose_name="payment amount",
        default=0
    )
    payment_usd_left = models.FloatField(
        verbose_name="payment left",
        default=0
    )
    paid = models.FloatField(
        verbose_name="paid",
        default=0
    )

    def count_payment(self):
        discount_amount = 0
        if self.discount:
            discount_amount = self.discount.amount_usd
        payment_amount = self.fee_category.amount_usd
        self.payment_usd = payment_amount - discount_amount
        self.payment_usd_left = payment_amount - discount_amount
        self.paid = 0
        return True
    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name}-{self.fee_category.title}"

    class Meta:
        verbose_name = "Fee"
        verbose_name_plural = "Fees"

class PaymentPlan(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="payment_plans",
        verbose_name="student"
    )
    fee = models.ForeignKey(
        Fee,
        on_delete=models.CASCADE,
        related_name="payment_plans",
        verbose_name="fee"
    )
    date = models.DateField(
        blank=False,
        null=False,
        verbose_name="date"
    )
    amount = models.FloatField(
        blank=False,
        null=False,
        verbose_name="amount"
    )

    def __str__(self):
        return f"{self.date}-{self.amount}"

    class Meta:
        verbose_name = "Payment plan"
        verbose_name_plural = "Payment plans"

class PaymentCategory(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=200,
        verbose_name="slug"
    )
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="title"
    )
    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Payment category"
        verbose_name_plural = "Payments categories"



class PaymentType(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        max_length=200,
        verbose_name="slug"
    )
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="title"
    )
    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Payment type"
        verbose_name_plural = "Payment types"

class Payment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="student"
    )
    fee = models.ForeignKey(
        Fee,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="fee"
    )
    payment_category = models.ForeignKey(
        PaymentCategory,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="payment category"
    )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name="payment type"
    )
    amount_usd = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )
    rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="rate"
    )
    amount_kgz = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )
    who_paid = models.TextField(
        blank=False,
        null=False,
        verbose_name="who paid"
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="note"
    )

    def count_payment(self):
        if self.amount_kgz and self.rate and self.amount_usd:
            self.fee.payment_usd_left -= self.amount_usd
            self.fee.paid += self.amount_usd
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.amount_kgz += self.amount_kgz
            cashbox.total_income += self.amount_usd
            cashbox.save()
            self.fee.save()
            self.save()
            return True

        elif self.amount_usd and not self.amount_kgz and not self.rate:
            self.fee.payment_usd_left -= self.amount_usd
            self.fee.paid += self.amount_usd
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.amount_usd += self.amount_usd
            cashbox.total_income += self.amount_usd
            cashbox.save()
            self.fee.save()
            self.save()
            return True

        elif self.amount_kgz and self.rate and not self.amount_usd:
            amount_usd = self.amount_kgz // self.rate
            self.fee.payment_usd_left -= amount_usd
            self.fee.paid += amount_usd
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.amount_kgz += self.amount_kgz
            cashbox.total_income += amount_usd
            cashbox.save()
            self.amount_usd = amount_usd
            self.fee.save()
            self.save()
            return True
        else:
            return False






