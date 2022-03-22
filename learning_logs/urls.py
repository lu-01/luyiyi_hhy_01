"""learning_logs URL Configuration

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
from . import views   				# 从当前文件夹导入视图

# 可在learning_logs程序中请求的网页
urlpatterns = [	
	# 主页   learning_logs程序的URL (url, 视图函数, 名称)
    path('', views.index, name='index'), 
	 
	# 显示所有主题   使用正则表达式: r'^topics/$' = 'topics/',  r表示原始字符串
	re_path(r'^topics/$', views.topics, name='topics'),   

	# 特定主题的详细页面   ?P<topic_id>：将匹配的值存入topics_id， \d+:与任何数字匹配
	re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), 

	# 用于添加新主题的网页
	re_path(r'^new_topic/$', views.new_topic, name='new_topic'), 
	
	# 用于添加新条目的网页
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'), 
	
	# 用于编辑条目的网页
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'), 

]

