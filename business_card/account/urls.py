from django.conf.urls import patterns, url

from business_card.account.views import AccountLoginView, AccountLogoutView


urlpatterns = patterns('',

    url(r'^login/$',        AccountLoginView.as_view(), name='account.login'),
    url(r'^logout/$',       AccountLogoutView.as_view(), name='account.logout'),

)
