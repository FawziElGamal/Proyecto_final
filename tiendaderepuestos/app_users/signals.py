from .models import Client
from django.db.models.signals import pre_save
from django.dispatch import receiver
import os

@receiver(pre_save, sender=Client)
def delete_old_avatar_file(sender, instance, **kwargs):
    try:
        old_url = Client.objects.get(user_id=instance.user.id).avatar.url

        if instance.avatar and instance.avatar != old_url[7:]:
            old_path = Client.objects.get(user_id=instance.user.id).avatar.path

            if os.path.isfile(old_path) and old_url != "/media/app_users/avatars/noneavatar.png":
                os.remove(old_path)

    except:
        print("Cliente no encotrado. Puede tratarse de estar creandose el cliente por primera vez")