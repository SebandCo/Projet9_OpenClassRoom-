# Generated by Django 4.2.1 on 2023-06-18 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_critique_note"),
    ]

    operations = [
        migrations.AddField(
            model_name="critique",
            name="nombre_critique",
            field=models.IntegerField(default=0, verbose_name="Nombre de critique"),
        ),
    ]