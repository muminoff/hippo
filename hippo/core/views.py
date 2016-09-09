# Django
from django.views.generic import TemplateView, FormView, View, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Boto3 
import boto3
import boto3.session


class SignupForm(forms.ModelForm):
    username = forms.CharField(
        label=_('Username'),
        widget=forms.TextInput(
            attrs={
                'maxlength': 30,
                'title': _('Username'),
            },
        ),
        required=True,
    )
    first_name = forms.CharField(
        label=_('First name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'maxlength': 30,
                'title': _('First name'),
            },
        ),
    )
    last_name = forms.CharField(
        label=_('Last name'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'maxlength': 30,
                'title': _('Last name'),
            },

        ),
    )
    email = forms.CharField(
        label=_('Email'),
        required=True,
        widget=forms.TextInput(
            attrs={
                'title': _('Email'),
            }
        ),
    )
    password = forms.CharField(
        label=_('Password'),
        widget=forms.PasswordInput(
            attrs={
                'maxlength': 24,
                'title': _('Password'),
            }
        ),
        required=True,
    )
    password2 = forms.CharField(
        label=_('Password (again)'),
        widget=forms.PasswordInput(
            attrs={
                'maxlength': 24,
                'title': _('Password (again)'),
            }
        ),
        required=True,
    )

    class Meta:
        model = User
        exclude = ['date_joined', 'is_staff']


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request):
        return super(IndexView, self).get(request)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            session = boto3.session.Session()
            s3client = session.client(
                's3',
                endpoint_url=settings.BACKEND_ENDPOINT_URL)

            response = s3client.list_objects(
                Bucket=self.request.user.profile.bucket)
            context['objects'] = response['Contents']
            return context


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('workspace')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get(self, request):

        if request.user and request.user.is_authenticated():
            return HttpResponseRedirect(
                request.GET.get('next', reverse('workspace')))

        return super(LoginView, self).get(request)


class LogoutView(View):
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(self.success_url)


class SignupView(CreateView):
    template_name = 'user/signup.html'
    form_class = SignupForm
    model = User
    success_url = reverse_lazy('workspace')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_active = True
        user.save()
        return super(SignupView, self).form_valid(form)
