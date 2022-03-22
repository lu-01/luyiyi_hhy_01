"""users URL Configuration

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

from django.urls import path, re_path
from django.contrib.auth.views import LoginView  # 导入默认视图函数
from . import views   			  		# 从当前文件夹导入视图

# 可在users程序中请求的网页
urlpatterns = [	
	# 登陆页面   login是默认视图函数，故需要传递一个字典告诉模板在哪里
    re_path(r'^login/$', LoginView.as_view(template_name='users/login.html'), name='login'), 
	# 注销
    re_path(r'^logout/$', views.logout_view, name='logout'), 
    # 注册页面
    re_path(r'^register/$', views.register, name='register'), 
     
]
