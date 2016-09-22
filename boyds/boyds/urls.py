from django.conf.urls import include, url
from django.contrib import admin

from userprofile import views as profile_views

from dashboard import views as dashboard_views

urlpatterns = [
    # Examples:
    url(r'^$',
    	dashboard_views.DashboardView.as_view(),
    	name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/',
    	profile_views.login.LoginView.as_view(),
    	name='login'),
    url(r'^admin/',
    	include(admin.site.urls)),
]
