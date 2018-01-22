"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

import views
from mysite import views as view, settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', view.hello),
    url(r'^time/$', view.current_datetime),
    url(r'^time/plus/(\d{1,2})/$', view.hours_ahead, name='hours_ahead'),
    url(r'^url/$', view.current_url_view_good),
    url(r'^test/$', view.display_meta),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^contact/$', view.contact),
    url(r'^my_time/$', views.my_time),
    url(r'^xml/$', view.return_xml),
    url(r'^login', view.login_do),
    url(r'^registe', view.registe_do)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
