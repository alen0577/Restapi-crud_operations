# Generated by Django 4.1.2 on 2022-11-15 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_mobile_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='mobile_no',
            new_name='mobile',
        ),
    ]
