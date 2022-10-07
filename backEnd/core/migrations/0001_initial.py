# Generated by Django 4.1.2 on 2022-10-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('patronymic', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('sex', models.CharField(max_length=50)),
                ('is_married', models.CharField(choices=[('Y', 'Is married'), ('N', 'Is not married')], max_length=1)),
                ('role_id', models.PositiveIntegerField()),
            ],
        ),
    ]