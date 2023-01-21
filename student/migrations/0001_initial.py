# Generated by Django 4.1.5 on 2023-01-21 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('session', '0001_initial'),
        ('student_class', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=30, verbose_name="student's id")),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last name')),
                ('patronymic', models.CharField(max_length=50, verbose_name='patronymic')),
                ('gender', models.CharField(choices=[('male', 'male'), ('feamle', 'female')], max_length=50, verbose_name='gender')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='media/student_images', verbose_name='photo')),
                ('birthday', models.DateField(verbose_name='date of birth')),
                ('status', models.CharField(choices=[('graduated', 'graduated'), ('out of', 'out of'), ('not confirmed', 'not confirmed'), ('active', 'active'), ('pre-registered', 'pre-refistered')], max_length=50, verbose_name='status')),
                ('admission_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='session.session', verbose_name='academic year')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student_class.class', verbose_name='class')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.TextField(verbose_name='full name')),
                ('who', models.CharField(max_length=100, verbose_name='who')),
                ('address', models.TextField(verbose_name='address')),
                ('phone_number', models.CharField(max_length=20, verbose_name='phone number')),
                ('id_passport', models.CharField(blank=True, max_length=50, null=True, verbose_name='id passport')),
                ('work_place', models.TextField(blank=True, null=True, verbose_name='work place')),
                ('is_responsible', models.BooleanField(default=True, verbose_name='is responsible')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='student.student', verbose_name='family member')),
            ],
            options={
                'verbose_name': 'Family member',
                'verbose_name_plural': 'Family members',
            },
        ),
    ]
