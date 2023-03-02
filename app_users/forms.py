from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext_lazy as _


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

