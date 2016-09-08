from django.views.generic import TemplateView, FormView, View
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'index.html'


class LoginView(FormView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('workspace')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get(self, request):

        # if request.user and request.user.is_authenticated():
        #     return HttpResponseRedirect(
        #         request.GET.get('next', reverse('workspace')))

        return super(LoginView, self).get(request)


class LogoutView(View):
    success_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponseRedirect(self.success_url)
