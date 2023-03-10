# Generated by Django 4.1.5 on 2023-01-22 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student_class', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizenship',
            fields=[
                ('slug', models.SlugField(max_length=150, primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Citizenship',
                'verbose_name_plural': 'Citizenships',
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('slug', models.SlugField(max_length=150, primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Marital status',
                'verbose_name_plural': 'Marital status',
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('slug', models.SlugField(max_length=150, primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Nationality',
                'verbose_name_plural': 'Nationalities',
            },
        ),
        migrations.CreateModel(
            name='Specilaty',
            fields=[
                ('slug', models.SlugField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='slug')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
            ],
            options={
                'verbose_name': 'Specialty',
                'verbose_name_plural': 'Specialties',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='username')),
                ('password', models.CharField(blank=True, max_length=100, null=True, verbose_name='password')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('patronymic', models.CharField(max_length=50, verbose_name='patronymic')),
                ('birthday', models.DateField(verbose_name='date')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10, verbose_name='gender')),
                ('position', models.CharField(choices=[('director', 'director'), ('accountant', 'accountant'), ('staff', 'staff')], max_length=50, verbose_name='specialty')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/student_images', verbose_name='photo')),
                ('status', models.CharField(choices=[('????????????', '????????????'), ('????????????????', '????????????????'), ('???????????????? ?? ???????????? ??????????', '???????????????? ?? ???????????? ??????????'), ('?? ?????????????????? ??????????????', '?? ?????????????????? ??????????????'), ('???????????????? ???? ???????????? ??????????', '???????????????????????? ???? ???????????? ??????????????')], max_length=100, verbose_name='status')),
                ('citizenship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='staff.citizenship', verbose_name='citizenship')),
                ('class_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staffs', to='student_class.class', verbose_name='class')),
                ('marital_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='staff.maritalstatus', verbose_name='marital status')),
                ('nationality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='staff.nationality', verbose_name='nationality')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='staff.specilaty', verbose_name='nationality')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='StaffContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthplace', models.TextField(blank=True, null=True, verbose_name='birthplace')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone number')),
                ('id_passport', models.CharField(blank=True, max_length=50, null=True, verbose_name='id passport')),
                ('issuing_authority', models.TextField(blank=True, null=True, verbose_name='issuing authority')),
                ('date_of_issue', models.DateField(blank=True, null=True, verbose_name='date of issue')),
                ('inn', models.CharField(blank=True, max_length=100, null=True, verbose_name='inn')),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='staff_contact_info', to='staff.staff', verbose_name='staff')),
            ],
            options={
                'verbose_name': "Staff's contact information",
                'verbose_name_plural': "Staff's contact informations",
            },
        ),
    ]
