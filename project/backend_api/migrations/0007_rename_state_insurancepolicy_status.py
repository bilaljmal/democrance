# Generated by Django 4.2.2 on 2024-01-29 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0006_alter_insurancepolicy_cover_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='insurancepolicy',
            old_name='state',
            new_name='status',
        ),
    ]
