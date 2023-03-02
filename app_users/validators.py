from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def file_size_validate(value):
    """ Validator. Checks the size of the downloaded file """
    file_size = value.size
    max_megabytes = 5.0
    if file_size > max_megabytes * 1024 * 1024:
        raise ValidationError(_(f"Download error: the file size is allowed to be no more than {max_megabytes} MB"))
