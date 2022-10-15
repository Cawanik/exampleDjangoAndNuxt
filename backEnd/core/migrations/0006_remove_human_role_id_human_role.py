# Generated by Django 4.1.2 on 2022-10-14 22:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_human_role_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='role_id',
        ),
        migrations.AddField(
            model_name='human',
            name='role',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.PROTECT, related_name='role', to='core.role'),
            preserve_default=False,
        ),
    ]