from django.contrib.auth.models import AbstractBaseUser, Group
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator, FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from app_users.managers import CustomUserManager
from app_users.validators import file_size_validate


class CustomUser(AbstractBaseUser, PermissionsMixin):
    image_validator = FileExtensionValidator(
        allowed_extensions=['png', 'jpg', 'jpeg'],
        message=_('Download error: Only files with the following extensions are allowed: .jpg .jpeg .png')
    )

    email = models.EmailField('email', unique=True, db_index=True)
    email_confirmed = models.BooleanField(_('email confirmed'), default=False)
    username = models.SlugField(_('username'), max_length=55, db_index=True, unique=True, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=55, blank=True, db_index=True)
    first_name = models.CharField(_('first name'), max_length=55, blank=True, db_index=True)
    patronymic = models.CharField(_('patronymic'), max_length=55, blank=True, db_index=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True, db_index=True)
    is_active = models.BooleanField(_('is active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    profile_image = models.ImageField(_('profile image'), upload_to='avatars/%Y/%m/%d/', null=True, blank=True,
                                      validators=[image_validator, file_size_validate])
    phone_regex = RegexValidator(regex=r'^\+\d{11,20}',
                                 message=_("The phone number must be specified in the following format: '+79012345678'."))
    phone_number = models.CharField(validators=[phone_regex], max_length=20, blank=True,
                                    verbose_name=_('phone number'), db_index=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email


class ProxyGroups(Group):
    class Meta:
        proxy = True
        verbose_name = _('group')
        verbose_name_plural = _('groups')
