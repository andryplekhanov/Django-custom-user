from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from app_users.forms import UserLoginForm, ResetPasswordForm, PasswordSetForm


class LogInView(LoginView):
    """ Log in to your account View """
    template_name = 'app_users/login.html'
    authentication_form = UserLoginForm
    next_page = reverse_lazy('home')
    extra_context = {'title': _('Log In')}


class LogOutView(LogoutView):
    """ Log Out View """
    next_page = reverse_lazy('home')


class ResetPasswordView(PasswordResetView):
    email_template_name = 'app_users/password_reset_email.html'
    template_name = 'app_users/password_reset_form.html'
    form_class = ResetPasswordForm
    extra_context = {'title': _('Password Reset')}


class ResetPasswordDoneView(PasswordResetDoneView):
    template_name = 'app_users/password_reset_done.html'
    extra_context = {'title': _('Password Reset Done')}


class ResetPasswordConfirmView(PasswordResetConfirmView):
    template_name = 'app_users/password_reset_confirm.html'
    form_class = PasswordSetForm
    post_reset_login = False
    extra_context = {'title': _('Password Reset Confirm')}

    def get_success_url(self):
        return reverse_lazy('password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    template_name = 'app_users/password_reset_complete.html'
    extra_context = {'title': _('Password Reset Complete')}
