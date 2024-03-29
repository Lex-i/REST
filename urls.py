"""rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from rest_framework import routers
from restapp.views import TaskViewSet, CreateUserView

router = routers.DefaultRouter()
# router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)
# router.register(r'due_task', DueTaskViewSet)
# router.register(r'completed_task', CompletedTaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^register/$', CreateUserView.as_view(), name='user'),
    re_path(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework')),
    re_path(r'^', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
