# Generated by Django 5.0.1 on 2024-09-30 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_date_updated'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='assigent_to',
            new_name='assiged_to',
        ),
    ]
