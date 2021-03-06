"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

# 包含项目中的应用程序的URL
urlpatterns = [			
    path('admin/', admin.site.urls),	# admin.site.urls模块定义了可在管理网站中请求的所有URL
    path('', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),  # learning_logs程序的URL
	path('users/', include(('users.urls', 'users'), namespace='users')),  # users程序的URL
	
]
