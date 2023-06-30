# Generated by Django 4.2.1 on 2023-06-24 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "authentication",
            "0002_remove_user_nombre_post_user_nombre_critique_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    {"Utilisateur", "UTILISATEUR"},
                    {"ADMINISTRATEUR", "Administrateur"},
                ],
                max_length=30,
            ),
        ),
    ]
