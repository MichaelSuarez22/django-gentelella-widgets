# Generated by Django 4.2.4 on 2023-09-11 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_custompermission'),
        ('djgentelella', '00012_defaultusecompessstatic'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionRelated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('related_permissions', models.ManyToManyField(related_name='permission_dep', to='auth.permission')),
            ],
        ),
    ]
