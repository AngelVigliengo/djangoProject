# Generated by Django 3.2.13 on 2022-05-22 18:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0004_student_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfCall', models.DateField(default=datetime.datetime(2022, 5, 22, 19, 41, 37, 335412), verbose_name='Date of Call')),
                ('reason', models.CharField(default='', help_text='Reason about student missing', max_length=255, verbose_name='reason')),
                ('isMissing', models.BooleanField(default=True, help_text='Student missing ?', verbose_name='isMissing')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Student', to='lycee.student')),
            ],
        ),
    ]