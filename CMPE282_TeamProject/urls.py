"""CMPE272_Maverick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.http import HttpResponse

admin.site.site_header = 'CMPE282 - Employees Portal'

def health_check(request): return  HttpResponse(status=200)

urlpatterns = [
	path('health', health_check),
	path('admin/', admin.site.urls),
	path('api/employee/', include('apps.employees.urls')),
	path('', include('apps.frontend.urls')),
	path('', include('django_sso.sso_gateway.urls')),
]
