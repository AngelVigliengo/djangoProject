# Generated by Django 3.2.13 on 2022-04-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='aucun', max_length=50, null=True)),
                ('year_from_bac', models.SmallIntegerField(default=0, help_text='year since le bac', null=True, verbose_name='year')),
                ('scholar_year', models.CharField(default='0000-00001', max_length=9, null=True)),
            ],
        ),
    ]
