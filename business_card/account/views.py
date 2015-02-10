from django.contrib.auth import logout, login
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseNotAllowed
from django.shortcuts import redirect

from business_card.account.forms import AccountLoginForm, AccountRegisterForm
from business_card.core.views import TemplateView


class AccountLoginView(TemplateView):

    template_name = 'account/account-login.html'

    def get(self, request):
        return self.render_to_response({'form': AccountLoginForm()})

    def post(self, request):
        form = AccountLoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            next = request.POST.get('next', reverse('business_card.home'))
            return redirect(next)

        return self.render_to_response({'form': form})


class AccountLogoutView(TemplateView):

    def get(self, request):
        return HttpResponseNotAllowed(permitted_methods=['post'])

    def post(self, request):
        logout(request)
        return redirect('business_card.home')


class AccountRegisterView(TemplateView):

    template_name = 'account/account-register.html'

    def get(self, request):
        return self.render_to_response({'form': AccountRegisterForm()})

    def post(self, request):
        form = AccountRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('business_card.home')
        return self.render_to_response({
            'form': form,
        })
