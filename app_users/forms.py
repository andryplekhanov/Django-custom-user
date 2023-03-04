from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm, \
    UserChangeForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(max_length=250, required=True, label='email',
                                widget=forms.TextInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'require',
                                    'maxlength': '250',
                                    'placeholder': _('Enter your e-mail'),
                                    'autocomplete': 'email'
                                }))
    password = forms.CharField(max_length=150, label=_('password'), required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-input',
                                   'data-validate': 'require',
                                   'placeholder': _('Enter your password'),
                                   'autocomplete': 'password',
                                   'maxlength': '150'}))


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(max_length=150, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'data-validate': 'requirePassword',
                                                                  'placeholder': _('Enter your password'),
                                                                  'autocomplete': 'new-password',
                                                                  'maxlength': '150'}))
    password2 = forms.CharField(max_length=150, required=True,
                                widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                  'data-validate': 'requireRepeatPassword',
                                                                  'placeholder': _('Enter your password again'),
                                                                  'autocomplete': 'new-password',
                                                                  'maxlength': '150'}))
    email = forms.EmailField(max_length=255, label='e-mail', required=True,
                             widget=forms.TextInput(attrs={'class': 'form-input',
                                                           'data-validate': 'requireMail',
                                                           'placeholder': _('Enter your e-mail'),
                                                           'maxlength': '255'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=55, required=False, label=_('First name'),
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-input',
                                     'data-validate': 'require',
                                     'placeholder': _('Enter your first name'),
                                     'maxlength': '55'
                                 }))
    last_name = forms.CharField(max_length=55, required=False, label=_('Last name'),
                                widget=forms.TextInput(attrs={
                                    'class': 'form-input',
                                    'data-validate': 'require',
                                    'placeholder': _('Enter your last name'),
                                    'maxlength': '55'
                                }))
    patronymic = forms.CharField(max_length=55, required=False, label=_('Patronymic'),
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-input',
                                     'data-validate': 'require',
                                     'placeholder': _('Enter your patronymic'),
                                     'maxlength': '55'
                                 }))
    username = forms.SlugField(max_length=55, required=False, label=_('Username'),
                               widget=forms.TextInput(attrs={
                                   'class': 'form-input',
                                   'data-validate': 'require',
                                   'placeholder': _('Enter your username'),
                                   'maxlength': '55'
                               }))
    email = forms.EmailField(max_length=250, label='email', required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-input',
                                 'data-validate': 'require',
                                 'maxlength': '250',
                                 'placeholder': _('Enter your email'),
                             }))
    phone_number = forms.CharField(required=False, label=_('Phone number'),
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-input',
                                       'placeholder': _('Enter your phone number'),
                                   }))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name', 'patronymic', 'phone_number')


class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(max_length=250, required=True,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-input',
                                 'data-validate': 'require',
                                 'maxlength': '250',
                                 'autocomplete': 'email'
                             }))


class PasswordSetForm(SetPasswordForm):
    new_password1 = forms.CharField(max_length=150, strip=False, required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-input',
                                        'data-validate': 'requirePassword',
                                        'placeholder': _('Enter a new password'),
                                        'autocomplete': 'new-password',
                                        'maxlength': '150'
                                    }))
    new_password2 = forms.CharField(max_length=150, required=True, strip=False,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-input',
                                        'data-validate': 'requireRepeatPassword',
                                        'placeholder': _('Enter a new password again'),
                                        'autocomplete': 'new-password',
                                        'maxlength': '150'
                                    }))
