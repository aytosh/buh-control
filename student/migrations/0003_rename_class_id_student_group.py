# Generated by Django 4.1.6 on 2023-02-09 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_familymember_student_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='class_id',
            new_name='group',
        ),
    ]