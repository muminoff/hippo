# Django
from django.conf.urls import url
from django.contrib import admin

# Hippo
from core.views import IndexView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='workspace'),
]
