# Generated by Django 3.1 on 2020-08-31 15:33

import demoapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0005_a_abcde_b_c_d_e'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputMask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('phone', models.CharField(max_length=14, validators=[demoapp.models.validate_inputs])),
                ('serial_number', models.CharField(max_length=23, validators=[demoapp.models.validate_inputs])),
                ('taxid', models.CharField(max_length=11, validators=[demoapp.models.validate_inputs])),
                ('credit_card', models.CharField(max_length=19, validators=[demoapp.models.validate_credit_card])),
                ('email', models.EmailField(max_length=254, validators=[demoapp.models.validate_email])),
            ],
        ),
    ]