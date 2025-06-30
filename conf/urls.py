from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from .redirect.signin import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('api/', include(('skillhub.conf.urls', 'skillhub'), namespace='skillhub')),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)