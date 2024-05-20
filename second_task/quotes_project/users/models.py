from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """
    Profile model extends the built-in User model with additional data,
    providing personal and contact information, along with a custom avatar.

    Attributes:
        user (OneToOneField): Links each Profile uniquely to a Django User
                              model instance. Ensures one-to-one relationship
                              with cascade delete.
        avatar (ImageField): Stores an image file representing the user's
                             avatar. Defaults to 'default_avatar.png' and
                             stored in 'profile_images' directory.
        first_name (CharField): Optional field for the user's first name.
        last_name (CharField): Optional field for the user's last name.
        email (EmailField): Optional field for the user's email address.
        phone_number (CharField): Optional field for the user's phone number,
                                  formatted as a string.
        birth_date (DateField): Optional field for the user's date of birth,
                                allows null values.

    Methods:
        __str__(self):
            Returns the username of the user associated with this profile,
            aiding in admin display and debugging.
        save(self, *args, **kwargs):
            Extends the default save method to include image resizing.
            Resizes the uploaded avatar to a maximum of 250x250 pixels if
            the image dimensions exceed this size, ensuring uniformity and
            conserving storage.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        default='default_avatar.png',
        upload_to='profile_images'
    )
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        """
        Return the username of the user associated with this profile.
        """
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        """
        Extends the default save method.
        If the avatar is larger than 250x250 pixels, it is resized to these
        dimensions before saving, helping to conserve storage.
        """
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 250 or img.width > 250:
            new_img = (250, 250)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
