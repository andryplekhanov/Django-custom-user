from django.urls import path
from django.views.generic import TemplateView

from app_users.views import *

urlpatterns = [
    path('login/', LogInView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path("signup/", SignUp.as_view(), name="signup"),

    # path('profile/', account_view, name='profile'),
    # path('profile/edit/', EditProfileView.as_view(), name='edit_profile'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset/done/', ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset/complete/', ResetPasswordCompleteView.as_view(), name='password_reset_complete'),

    path('invalid_verify/', TemplateView.as_view(template_name='app_users/invalid_verify.html'), name='invalid_verify'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(template_name='app_users/confirm_email.html'), name='confirm_email'),
]
