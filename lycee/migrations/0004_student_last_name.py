# Generated by Django 3.2.13 on 2022-04-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0003_auto_20220413_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='???', help_text='last name of the student', max_length=255, verbose_name='lastname'),
        ),
    ]
