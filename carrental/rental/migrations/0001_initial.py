# Generated by Django 5.0.6 on 2024-05-08 12:21

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('post_code', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('building_no', models.CharField(max_length=20)),
                ('appartment_no', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('engine_type', models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20)),
                ('seats_count', models.PositiveSmallIntegerField()),
                ('dors_count', models.PositiveSmallIntegerField()),
                ('fuel_usage', models.FloatField()),
                ('engine_power', models.PositiveSmallIntegerField()),
                ('color', models.CharField(max_length=20)),
                ('gearbox_type', models.CharField(choices=[('benzynowy', 'Benzynowy'), ('diesel', 'Diesel'), ('hybrydowy', 'Hybrydowy'), ('elektryczny', 'Elektryczny'), ('wodorowy', 'Wodorowy')], max_length=20)),
                ('available', models.BooleanField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('equipment', models.ManyToManyField(to='rental.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone', models.CharField(max_length=20)),
                ('identity_document_type', models.CharField(choices=[('dowod', 'dowód osobisty'), ('paszport', 'paszport'), ('prawo_jazdy', 'prawo jazdy')], max_length=20)),
                ('identity_document_no', models.CharField(max_length=20)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='rental.address')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('declared_order_duration', models.DurationField()),
                ('pickup_date', models.DateTimeField()),
                ('return_date', models.DateTimeField()),
                ('deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('karta', 'Karta'), ('gotowka', 'Gotowka'), ('przelew', 'Przelew'), ('blik', 'Blik')], max_length=20)),
                ('payment_status', models.BooleanField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rental.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='rental.user')),
            ],
        ),
    ]
