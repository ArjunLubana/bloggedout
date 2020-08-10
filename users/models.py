from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            width, height = img.size   # Get dimensions
            d = 1000
            img = img.crop(((width - d) // 2,
                         (height - d) // 2,
                         (width + d) // 2,
                         (height + d) // 2))
            img = img.resize((300, 300))
            img.save(self.image.path)
