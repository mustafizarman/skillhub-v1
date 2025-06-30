from django.contrib.auth.models import AbstractUser
from django.db import models
from .role import get_default_role  # import only the function, not Role class
from django.core.validators import FileExtensionValidator

class User(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        'skillhub.Role',  # use string reference here, replace 'skillhub' with your app name
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=get_default_role
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        null=True,
        blank=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )

    birthday = models.DateField(null=True, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

def get_superadmin_user():
    from .role import Role  # deferred import to avoid circular import
    try:
        superuser = User.objects.get(role=Role.objects.get(name='superadmin'))
        return superuser
    except User.DoesNotExist:
        return None
