# Generated by Django 4.1.5 on 2023-01-22 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accrual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_usd', models.FloatField(blank=True, null=True, verbose_name='amount usd')),
                ('amount_kgz', models.FloatField(blank=True, null=True, verbose_name='amount kgz')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
            ],
            options={
                'verbose_name': 'Accrual',
                'verbose_name_plural': 'Accrual',
            },
        ),
        migrations.CreateModel(
            name='Cashbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_usd', models.FloatField(default=0, verbose_name='amount usd')),
                ('amount_kgz', models.FloatField(default=0, verbose_name='amount kgz')),
                ('total_income', models.FloatField(default=0, verbose_name='total income')),
                ('total_expenses', models.FloatField(default=0, verbose_name='total expenses')),
            ],
        ),
        migrations.CreateModel(
            name='ExpensesCategory',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.TextField(verbose_name='title')),
            ],
            options={
                'verbose_name': 'Expense category',
                'verbose_name_plural': 'Expense categories',
            },
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.TextField(verbose_name='title')),
            ],
            options={
                'verbose_name': 'Income category',
                'verbose_name_plural': 'Income categories',
            },
        ),
        migrations.CreateModel(
            name='SalaryCategory',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.TextField(verbose_name='title')),
                ('amount_usd', models.FloatField(blank=True, null=True, verbose_name='amount usd')),
            ],
            options={
                'verbose_name': 'Salary category',
                'verbose_name_plural': 'Salary categories',
            },
        ),
        migrations.CreateModel(
            name='SalaryPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('full_name', models.TextField(verbose_name='full name')),
                ('amount_usd', models.FloatField(blank=True, null=True, verbose_name='amount usd')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('salary_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='finance.salarycategory', verbose_name='salary category')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salary_payments', to='staff.staff', verbose_name='who accepted')),
            ],
            options={
                'verbose_name': 'Salary payment',
                'verbose_name_plural': 'Salary payments',
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('amount_usd', models.FloatField(blank=True, null=True, verbose_name='amount usd')),
                ('amount_kgz', models.FloatField(blank=True, null=True, verbose_name='amount kgz')),
                ('rate', models.FloatField(blank=True, null=True, verbose_name='rate')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('income_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='finance.incomecategory', verbose_name='income category')),
                ('who_accepted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='incomes', to='staff.staff', verbose_name='who accepted')),
            ],
            options={
                'verbose_name': 'Income',
                'verbose_name_plural': 'Income',
            },
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('amount_usd', models.FloatField(blank=True, null=True, verbose_name='amount usd')),
                ('amount_kgz', models.FloatField(blank=True, null=True, verbose_name='amount kgz')),
                ('rate', models.FloatField(blank=True, null=True, verbose_name='rate')),
                ('note', models.TextField(blank=True, null=True, verbose_name='note')),
                ('expenses_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='finance.expensescategory', verbose_name='expenses category')),
                ('who_accepted', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='staff.staff', verbose_name='who accepted')),
            ],
            options={
                'verbose_name': 'Expenses',
                'verbose_name_plural': 'Expenses',
            },
        ),
    ]
