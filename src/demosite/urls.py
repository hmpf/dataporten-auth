from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html')),
    url('', include('social.apps.django_app.urls', namespace='social')),
]
