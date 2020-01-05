from django.conf.urls import url
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import password_reset_done

urlpatterns = [
    url(r'^$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^done/$', password_reset_done, name='password_reset_done'),
    url(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        {'post_reset_confirm' : reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    url(r'^complete/$', PasswordResetCompleteView.as_view() , name='password_reset_complete')
]