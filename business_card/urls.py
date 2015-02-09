from django.conf.urls import patterns, include, url
from django.contrib import admin
from business_card.shop.views import ShopHomeView

urlpatterns = patterns('',
    url(r'^admin/',                     include(admin.site.urls)),

    url(r'^$',                          ShopHomeView.as_view(), name='index_view'),

    url(r'^account/',                   include('business_card.account.urls')),
)
