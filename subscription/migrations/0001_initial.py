# Generated by Django 2.2 on 2019-09-26 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('email', models.EmailField(max_length=150, verbose_name='email')),
                ('phone', models.PositiveIntegerField()),
                ('created', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Suscripción',
                'verbose_name_plural': 'Suscripciones',
                'ordering': ['-created'],
            },
        ),
    ]
