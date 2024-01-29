# Generated by Django 4.2.2 on 2024-01-24 14:45

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('data_of_birth', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('policy_type', models.CharField(choices=[('personal-accident', 'Personal Accident')], max_length=20)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cover', models.PositiveIntegerField()),
                ('state', models.CharField(choices=[('new', 'New'), ('quoted', 'Quoted'), ('active', 'Active')], max_length=10)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend_api.customers')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]