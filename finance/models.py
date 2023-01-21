from django.db import models
from staff.models import Staff
class Cashbox(models.Model):
    amount_usd = models.FloatField(
        default=0,
        verbose_name="amount usd"
    )
    amount_kgz = models.FloatField(
        default=0,
        verbose_name="amount kgz"
    )
    total_income = models.FloatField(
        default=0,
        verbose_name="total income"
    )
    total_expenses = models.FloatField(
        default=0,
        verbose_name="total expenses"
    )

class IncomeCategory(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
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
        verbose_name = "Income category"
        verbose_name_plural = "Income categories"

class ExpensesCategory(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
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
        verbose_name = "Expense category"
        verbose_name_plural = "Expense categories"

class Income(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=False,
        null=False,
        verbose_name="date"
    )
    income_category = models.ForeignKey(
        IncomeCategory,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="incomes",
        verbose_name="income category"
    )
    amount_usd = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )
    amount_kgz = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount kgz"
    )
    rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="rate"
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="note"
    )
    who_accepted = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="incomes",
        verbose_name="who accepted"
    )

    def count_income(self):
        if self.amount_usd:
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.total_income += self.amount_usd
            cashbox.amount_usd += self.amount_usd
            cashbox.save()

        elif self.rate and self.amount_kgz:
            cashbox = Cashbox.objects.get(pk=1)
            amount_usd = self.rate * self.amount_kgz
            cashbox.total_income += amount_usd
            cashbox.amount_kgz += self.amount_kgz
            cashbox.save()

    def __str__(self):
        return f"{self.income_category}"

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Income"


class Expenses(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=False,
        null=False,
        verbose_name="date"
    )
    expenses_category = models.ForeignKey(
        ExpensesCategory,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="expenses",
        verbose_name="expenses category"
    )
    amount_usd = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )
    amount_kgz = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount kgz"
    )
    rate = models.FloatField(
        blank=True,
        null=True,
        verbose_name="rate"
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="note"
    )
    who_accepted = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="expenses",
        verbose_name="who accepted"
    )

    def count_expenses(self):
        if self.amount_usd:
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.total_expenses += self.amount_usd
            cashbox.amount_usd -= self.amount_usd
            cashbox.save()
        elif self.rate and self.amount_kgz:
            cashbox = Cashbox.objects.get(pk=1)
            amount_usd = self.rate * self.amount_kgz
            cashbox.total_expenses += amount_usd
            cashbox.amount_kgz -= self.amount_kgz
            cashbox.save()

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Expenses"
        verbose_name_plural = "Expenses"

class Accrual(models.Model):
    amount_usd = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )
    amount_kgz = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount kgz"
    )

    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="note"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=False,
        null=False,
        verbose_name="date"
    )

    def count_accrual(self):
        if self.amount_usd:
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.amount_usd += self.amount_usd
            cashbox.save()

        elif self.amount_kgz:
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.amount_kgz += self.amount_kgz
            cashbox.save()

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Accrual"
        verbose_name_plural = "Accrual"

class SalaryCategory(models.Model):
    slug = models.SlugField(
        primary_key=True,
        unique=True,
        verbose_name="slug"
    )
    title = models.TextField(
        blank=False,
        null=False,
        verbose_name="title"
    )
    amount_usd = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )

    def __str__(self):
        return f"{self.slug}"

    class Meta:
        verbose_name = "Salary category"
        verbose_name_plural = "Salary categories"

class SalaryPayment(models.Model):
    date = models.DateTimeField(
        auto_now_add=True,
        auto_now=False,
        blank=False,
        null=False,
        verbose_name="date"
    )
    full_name = models.TextField(
        blank=False,
        null=False,
        verbose_name="full name"
    )
    salary_category = models.ForeignKey(
        SalaryCategory,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="salaries",
        verbose_name="salary category"
    )
    amount_usd = models.FloatField(
        blank=True,
        null=True,
        verbose_name="amount usd"
    )
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name="note"
    )
    staff = models.ForeignKey(
        Staff,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="salary_payments",
        verbose_name="who accepted"
    )

    def count_salary(self):
        if self.amount_usd:
            cashbox = Cashbox.objects.get(pk=1)
            cashbox.amount_usd -= self.amount_usd
            cashbox.save()

    def __str__(self):
        return f"{self.full_name}"

    class Meta:
        verbose_name = "Salary payment"
        verbose_name_plural = "Salary payments"

