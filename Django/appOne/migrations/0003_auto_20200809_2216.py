# Generated by Django 3.0.1 on 2020-08-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOne', '0002_auto_20200809_2212'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationform',
            old_name='Passwd1',
            new_name='Passwd',
        ),
        migrations.RemoveField(
            model_name='registrationform',
            name='Passwd2',
        ),
    ]