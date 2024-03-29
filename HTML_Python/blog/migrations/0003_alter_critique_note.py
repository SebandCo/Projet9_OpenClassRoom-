# Generated by Django 4.2.1 on 2023-06-17 16:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_critique_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="critique",
            name="note",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "0"), (1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                default=0,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
