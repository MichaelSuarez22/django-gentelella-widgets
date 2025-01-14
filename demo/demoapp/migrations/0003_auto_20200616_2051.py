# Generated by Django 3.0.7 on 2020-06-16 20:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('demoapp', '0002_peoplegroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comunity',
            fields=[
                ('id',
                 models.AutoField(auto_created=True, primary_key=True, serialize=False,
                                  verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='peoplegroup',
            name='comunities',
            field=models.ManyToManyField(to='demoapp.Comunity'),
        ),
    ]
