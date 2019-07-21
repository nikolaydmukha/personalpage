from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authorization.urls')),
    path('main/', include('main.urls')),
    path('dummy/', include('main.urls')),
    path('block/', include('block.urls')),
    path('dpay/', include('dpay.urls')),
    path('pay_bcard/', include('pay_bcard.urls')),
    path('pay_sber/', include('pay_sber.urls')),
    path('profile_settings/', include('profile_settings.urls')),
    path('history_incomes/', include('history_incomes.urls')),
    path('your_messages/', include('your_messages.urls')),
    path('history_incomes/', include('history_incomes.urls')),
    path('history_traf/', include('history_traf.urls')),
    path('settings_inet/', include('settings_inet.urls')),
    path('settings_personal/', include('settings_personal.urls')),

]

#### FOR DJANGO-DEBUG-TOOOLBAR
from django.conf import settings
from django.conf.urls import include, url

if settings.DEBUG:
   import debug_toolbar
   urlpatterns += [
       url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
#### FOR DJANGO-DEBUG-TOOOLBAR