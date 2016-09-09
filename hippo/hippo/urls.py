# Django
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

# Hippo
from core.views import (
    IndexView, SettingsView, LoginView, LogoutView, SignupView)

urlpatterns = [
    url(r'^$', login_required(IndexView.as_view()), name='workspace'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^settings/$', login_required(SettingsView.as_view()), name='settings'),  # noqa
]
