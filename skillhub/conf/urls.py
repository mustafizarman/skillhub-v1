from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from skillhub.views.profile import *
from skillhub.controllers.profileController import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
     path('admin/', admin.site.urls),
    # path('roles/',RoleListView.as_view(), name="superadmindashboard"),
    # path('users/', UserListView.as_view(), name='user-list'),
    path('profile/', ProfileController.as_view(), name='user-profile'),
    # path('skills-detail/', SkillDetailView.as_view(), name='skill-detail'),
    

    # path('superadmin/', TemplateView.as_view(template_name='superadmin_page.html'),name="super-admin"),
    # path('users/<int:user_id>/update-role/', update_user_role, name='update-user-role'),
     path('profile-page/', profile_page, name='user-profile-page'),
    # path('skills/', skill_page ,name='skills')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
