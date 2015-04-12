from django.conf.urls import include, url
from django.contrib import admin

from .views import RegistrationFormView

urlpatterns = [
    # Examples:
    # url(r'^$', 'wasatch_classic.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', RegistrationFormView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
]
