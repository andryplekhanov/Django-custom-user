from django.contrib.auth import login, get_user_model
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic import CreateView

from app_users.forms import UserLoginForm, ResetPasswordForm, PasswordSetForm, CustomUserCreationForm
from app_users.utils import send_email_for_verify, authenticate_user

User = get_user_model()


class LogInView(LoginView):
    """
    Log in to your account View.
    If the user is registered, but his email is not confirmed,
    then we send him a confirmation email again.
    """
    template_name = 'app_users/login.html'
    authentication_form = UserLoginForm
    next_page = reverse_lazy('home')
    extra_context = {'title': _('Log In')}

    def form_valid(self, form):
        user = form.get_user()
        if not user.email_confirmed:
            send_email_for_verify(self.request, user)
            return HttpResponseRedirect(reverse('confirm_email'))
        return super().form_valid(form)


class LogOutView(LogoutView):
    """ Log Out View """
    next_page = reverse_lazy('home')


class SignUp(CreateView):
    """ Sign Up View """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("confirm_email")
    template_name = "app_users/signup.html"
    extra_context = {'title': _('Sign Up')}

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save()
            user = authenticate_user(form)
            send_email_for_verify(request, user)
            return redirect('confirm_email')
        return super().post(request, *args, **kwargs)


class EmailVerify(View):
    """ Email Verification View """
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_confirmed = True
            user.save()
            login(request, user)
            return redirect('home')
        return redirect('invalid_verify')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                User.DoesNotExist, ValidationError):
            user = None
        return user


class ResetPasswordView(PasswordResetView):
    """ Password Reset View """
    email_template_name = 'app_users/password_reset_email.html'
    template_name = 'app_users/password_reset_form.html'
    form_class = ResetPasswordForm
    extra_context = {'title': _('Password Reset')}


class ResetPasswordDoneView(PasswordResetDoneView):
    """ Password Reset Done View """
    template_name = 'app_users/password_reset_done.html'
    extra_context = {'title': _('Password Reset Done')}


class ResetPasswordConfirmView(PasswordResetConfirmView):
    """ Password Reset Confirm View """
    template_name = 'app_users/password_reset_confirm.html'
    form_class = PasswordSetForm
    post_reset_login = False
    extra_context = {'title': _('Password Reset Confirm')}

    def get_success_url(self):
        return reverse_lazy('password_reset_complete')


class ResetPasswordCompleteView(PasswordResetCompleteView):
    """ Password Reset Complete View """
    template_name = 'app_users/password_reset_complete.html'
    extra_context = {'title': _('Password Reset Complete')}
