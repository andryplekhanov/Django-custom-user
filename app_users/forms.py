from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm
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
