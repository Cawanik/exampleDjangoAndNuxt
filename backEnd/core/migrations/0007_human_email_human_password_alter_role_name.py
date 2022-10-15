# Generated by Django 4.1.2 on 2022-10-15 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_human_role_id_human_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='human',
            name='email',
            field=models.EmailField(default='cawa@cawa.cawa', max_length=254),
        ),
        migrations.AddField(
            model_name='human',
            name='password',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]