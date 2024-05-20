from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a Profile instance automatically
    when a new User instance is created.

    Parameters:
        sender (Model): The model class that sent the signal.
        instance (User): The instance of the model that triggered the signal.
        created (bool): Boolean value that is True if a new record was created.
        **kwargs: Variable keyword arguments.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Signal receiver that saves the associated Profile instance
    whenever the User instance is saved.

    Parameters:
        sender (Model): The model class that sent the signal.
        instance (User): The instance of the model that triggered the signal.
        **kwargs: Variable keyword arguments.
    """
    instance.profile.save()
