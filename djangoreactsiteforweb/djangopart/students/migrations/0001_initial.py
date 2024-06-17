# Generated by Django 5.0.6 on 2024-06-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Name')),
                ('b_date', models.DateField()),
                ('study_type', models.CharField(max_length=16, verbose_name='StudyType')),
            ],
        ),
    ]
