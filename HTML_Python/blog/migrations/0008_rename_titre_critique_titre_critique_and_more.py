# Generated by Django 4.2.1 on 2023-06-24 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_alter_ticket_illustration"),
    ]

    operations = [
        migrations.RenameField(
            model_name="critique",
            old_name="titre",
            new_name="titre_critique",
        ),
        migrations.RenameField(
            model_name="ticket",
            old_name="titre",
            new_name="titre_ticket",
        ),
    ]
