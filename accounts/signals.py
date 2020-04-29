from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
# from accounts.models import Administrador

#
# def administrador_profile(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name='Administrador')
#         instance.groups.add(group)
#
#         Administrador.objects.create(
#             user=instance,
#             name=instance.username,
#         )
#         print('Profile created!')
#
#
# post_save.connect(administrador_profile, sender=User)
from egresados.models import Egresado


def egresado_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='egresado')
        instance.groups.add(group)

        Egresado.objects.create(
            user=instance,
            name=instance.username,
        )
        print('Profile created!')


post_save.connect(egresado_profile, sender=User)