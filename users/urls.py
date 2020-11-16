from django.urls import path
#from . import views
from django.contrib.auth import views as auth_views
from .views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html')),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
