# Generated by Django 4.2.1 on 2023-07-01 06:35
from django.db import migrations

def create_groups(apps, schema_migration):
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    gestion_utilisateur = Permission.objects.get(codename='gestion_utilisateur')
    
    creator_permissions = [
        gestion_utilisateur
    ]
    
    administrateur = Group(name='Administrateur')
    administrateur.save()
    administrateur.permissions.set(creator_permissions)

    utilisateur = Group(name='Utilisateur')
    utilisateur.save()

    
    for user in User.objects.all():
        if user.role == 'Administrateur':
            administrateur.user_set.add(user)
        if user.role == 'Utilisateur':
            utilisateur.user_set.add(user)


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_auto_20230630_2302"),
    ]

    operations = [migrations.RunPython(create_groups)]
