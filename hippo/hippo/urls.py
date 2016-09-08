# Django
from django.conf.urls import url

# Hippo
from core.views import IndexView, LoginView, LogoutView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='workspace'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
