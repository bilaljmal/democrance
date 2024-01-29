# Generated by Django 4.2.2 on 2024-01-29 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_rename_state_insurancepolicy_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepolicy',
            name='status',
            field=models.CharField(blank=True, choices=[('new', 'New'), ('quoted', 'Quoted'), ('active', 'Active')], default='quoted', max_length=10),
        ),
    ]