from django.conf.urls import patterns, url

from business_card.account.views import AccountLoginView, AccountLogoutView, AccountRegisterView


urlpatterns = patterns('',

    url(r'^login/$',            AccountLoginView.as_view(), name='account.login'),
    url(r'^logout/$',           AccountLogoutView.as_view(), name='account.logout'),
    url(r'^register/$',         AccountRegisterView.as_view(), name='account.register'),

)
