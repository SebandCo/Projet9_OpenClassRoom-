# Generated by Django 4.2.1 on 2023-07-03 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_ticket_liste_contributeur"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="liste_contributeur",
            field=models.JSONField(blank=True),
        ),
    ]
